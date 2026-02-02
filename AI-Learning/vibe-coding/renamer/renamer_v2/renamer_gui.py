import os
import re
import yaml
import sys
import subprocess
from pathlib import Path
from datetime import datetime
from PyQt6.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
                             QLineEdit, QPushButton, QTextEdit, QMessageBox, QFileDialog)
from PyQt6.QtGui import QFont, QColor, QPalette, QIcon
from PyQt6.QtCore import Qt, QThread, pyqtSignal


# -------------------------- 后台处理线程（避免UI卡顿）--------------------------
class RenameThread(QThread):
    # 信号：更新日志、统计信息、处理完成
    log_signal = pyqtSignal(str)
    stat_signal = pyqtSignal(int, int, list)
    finish_signal = pyqtSignal()

    def __init__(self, root_dir):
        super().__init__()
        self.root_dir = root_dir
        self.total_files = 0
        self.modified_files = 0
        self.unmodified_files = []
        self.modified_paths = []  # 存储已修改文件路径

    def load_config(self, config_path):
        """加载配置文件"""
        try:
            with open(config_path, 'r', encoding='utf-8') as f:
                config = yaml.safe_load(f)
            if not isinstance(config, dict):
                raise ValueError("配置格式错误：需为 '分组: [关键词列表]' 格式")
            
            # 标准化配置
            normalized_config = {}
            for group, keywords in config.items():
                if not isinstance(keywords, list):
                    keywords = [str(keywords).strip()]
                normalized_config[group] = [str(kw).strip() for kw in keywords if str(kw).strip()]
            return normalized_config
        except FileNotFoundError:
            self.log_signal.emit("❌ 错误：未找到 config.yaml 文件")
            return None
        except Exception as e:
            self.log_signal.emit(f"❌ 配置错误：{str(e)}")
            return None

    def remove_prefix(self, filename):
        """移除已有的★分组★前缀"""
        return re.sub(r'^★.*?★', '', filename)

    def rename_files(self, current_dir, config):
        """递归处理文件"""
        for entry in os.scandir(current_dir):
            if entry.is_dir(follow_symlinks=False):
                self.rename_files(entry.path, config)
            elif entry.is_file():
                filename = entry.name
                file_path = entry.path

                # 跳过自身（EXE）
                if filename == Path(sys.argv[0]).name and current_dir == self.root_dir:
                    continue

                self.total_files += 1
                modified = False
                original_name = self.remove_prefix(filename)

                # 匹配关键词并修改
                for group, keywords in config.items():
                    for kw in keywords:
                        if kw in original_name:
                            new_name = f"★{group}★{original_name}"
                            new_path = os.path.join(current_dir, new_name)
                            if new_path != file_path:
                                try:
                                    os.rename(file_path, new_path)
                                    log_msg = f"✅ 已更新：{file_path} → {new_path}"
                                    self.log_signal.emit(log_msg)
                                    self.modified_files += 1
                                    self.modified_paths.append(f"{file_path} → {new_path}")
                                    modified = True
                                except Exception as e:
                                    self.log_signal.emit(f"❌ 失败：{file_path} - {str(e)}")
                            break
                    if modified:
                        break

                # 记录未修改文件
                if not modified:
                    self.unmodified_files.append(file_path)

    def run(self):
        """线程执行入口：从程序目录加载配置文件"""
        # 获取程序所在目录（与 UI 中逻辑一致）
        if getattr(sys, 'frozen', False):
            program_dir = os.path.dirname(sys.executable)
        else:
            program_dir = os.path.dirname(os.path.abspath(__file__))
        # 配置文件路径（程序同级目录）
        config_path = os.path.join(program_dir, "config.yaml")
        
        config = self.load_config(config_path)
        if not config:
            self.finish_signal.emit()
            return

        self.log_signal.emit(f"📂 开始处理根目录：{self.root_dir}")
        self.rename_files(self.root_dir, config)

        # 发送统计信息
        self.stat_signal.emit(self.total_files, self.modified_files, self.unmodified_files)
        # 发送已修改文件列表
        self.log_signal.emit(f"\n📊 处理完成：共扫描 {self.total_files} 个文件，修改 {self.modified_files} 个")
        self.finish_signal.emit()


# -------------------------- 主UI窗口 --------------------------
class RenameMainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.rename_thread = None  # 后台线程对象
        self.set_window_icon()  # 初始化时设置图标

    def init_ui(self):
        """初始化UI布局和样式"""
        # 窗口基础设置
        self.setWindowTitle("文件批量分级重命名工具")
        self.setGeometry(100, 100, 1000, 700)  # 位置(x,y) + 大小(w,h)
        self.setMinimumSize(800, 600)

        # 中心部件和主布局
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setSpacing(20)
        main_layout.setContentsMargins(30, 30, 30, 30)

        # -------------------------- 1. 根目录输入区域 --------------------------

        input_layout = QHBoxLayout()
        # 取消布局对按钮尺寸的压缩（关键：设置布局对齐方式，不强制拉伸）
        input_layout.setAlignment(Qt.AlignmentFlag.AlignLeft)
        input_layout.setSpacing(15)  # 输入框和按钮间距

        # 输入框（椭圆形，保持原有功能）
        self.dir_input = QLineEdit()
        self.dir_input.setPlaceholderText("请输入待处理根目录的绝对路径（例如：D:\\项目资料）")
        self.dir_input.setStyleSheet("""
            QLineEdit {
                border: 2px solid #4a90e2;
                border-radius: 30px;  /* 输入框也同步增大圆角，视觉统一 */
                padding: 0 25px;
                height: 60px;  /* 输入框高度与按钮一致 */
                font-size: 16px;
                background-color: #f8f9fa;
                min-width: 500px;  /* 输入框最小宽度，避免过窄 */
            }
            QLineEdit:focus {
                    border-color: #2962ff;
                background-color: white;
                outline: none;
            }
        """)
        input_layout.addWidget(self.dir_input)  # 移除stretch，避免强制拉伸

        # 选择目录按钮（强制椭圆+固定尺寸，解决样式失效问题）
        self.select_dir_btn = QPushButton("📂 选择目录")
        # 1. 强制固定按钮尺寸（宽x高），确保圆角能正常显示为椭圆
        self.select_dir_btn.setFixedSize(180, 60)  # 宽度180，高度60 → 配合30px圆角正好是椭圆
        # 2. 样式表增加 !important 提升优先级，防止被覆盖
        self.select_dir_btn.setStyleSheet("""
            QPushButton {
                border: none !important;  /* 强制取消边框 */
                border-radius: 30px !important;  /* 圆角=高度的一半，完美椭圆 */
                background-color: #4a90e2 !important;
                color: white !important;
                font-size: 16px !important;
                font-weight: 600 !important;
                text-align: center !important;
            }
            QPushButton:hover {
                background-color: #2962ff !important;
            }
            QPushButton:pressed {
                background-color: #1e40af !important;
            }
            /* 禁用默认的按钮焦点边框，避免影响椭圆视觉 */
            QPushButton:focus {
                outline: none !important;
                border: none !important;
            }
        """)
        self.select_dir_btn.clicked.connect(self.select_directory)
        input_layout.addWidget(self.select_dir_btn)

        main_layout.addLayout(input_layout)

        # -------------------------- 2. 功能按钮区域 --------------------------
        btn_layout = QHBoxLayout()
        
        # 处理按钮（椭圆形，强调色）
        self.process_btn = QPushButton("▶️ 开始处理")
        self.process_btn.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 25px;  /* 椭圆形 */
                background-color: #28a745;
                color: white;
                padding: 0 30px;
                height: 50px;
                font-size: 16px;
                font-weight: 600;
            }
            QPushButton:hover {
                background-color: #218838;
            }
            QPushButton:pressed {
                background-color: #1e7e34;
            }
            QPushButton:disabled {
                background-color: #6c757d;
            }
        """)
        self.process_btn.clicked.connect(self.start_process)
        btn_layout.addWidget(self.process_btn, stretch=1)

        # 修改配置按钮（椭圆形）
        self.config_btn = QPushButton("⚙️ 修改配置文件")
        self.config_btn.setStyleSheet("""
            QPushButton {
                border: none;
                border-radius: 25px;  /* 椭圆形 */
                background-color: #ffc107;
                color: #212529;
                padding: 0 30px;
                height: 50px;
                font-size: 16px;
                font-weight: 600;
                margin-left: 20px;
            }
            QPushButton:hover {
                background-color: #e0a800;
            }
            QPushButton:pressed {
                background-color: #c69500;
            }
        """)
        self.config_btn.clicked.connect(self.open_config)
        btn_layout.addWidget(self.config_btn, stretch=1)

        main_layout.addLayout(btn_layout)

        # -------------------------- 3. 信息显示区域（三列布局） --------------------------
        display_layout = QHBoxLayout()
        display_layout.setSpacing(20)

        # 3.1 统计信息显示框（椭圆形边框）
        self.stat_display = QTextEdit()
        self.stat_display.setReadOnly(True)
        self.stat_display.setPlaceholderText("处理统计信息将显示在这里...")
        self.stat_display.setStyleSheet("""
            QTextEdit {
                border: 2px solid #6c757d;
                border-radius: 15px;  /* 椭圆形 */
                padding: 15px;
                font-size: 14px;
                background-color: #f8f9fa;
            }
        """)
        display_layout.addWidget(self.stat_display, stretch=1)

        # 3.2 已修改文件显示框（椭圆形边框）
        self.modified_display = QTextEdit()
        self.modified_display.setReadOnly(True)
        self.modified_display.setPlaceholderText("已修改的文件路径将显示在这里...")
        self.modified_display.setStyleSheet("""
            QTextEdit {
                border: 2px solid #28a745;
                border-radius: 15px;  /* 椭圆形 */
                padding: 15px;
                font-size: 14px;
                background-color: #f8f9fa;
            }
        """)
        display_layout.addWidget(self.modified_display, stretch=1)

        # 3.3 未修改文件显示框（椭圆形边框）
        self.unmodified_display = QTextEdit()
        self.unmodified_display.setReadOnly(True)
        self.unmodified_display.setPlaceholderText("未修改的文件路径将显示在这里...")
        self.unmodified_display.setStyleSheet("""
            QTextEdit {
                border: 2px solid #dc3545;
                border-radius: 15px;  /* 椭圆形 */
                padding: 15px;
                font-size: 14px;
                background-color: #f8f9fa;
            }
        """)
        display_layout.addWidget(self.unmodified_display, stretch=1)

        main_layout.addLayout(display_layout, stretch=1)  # 占主要高度

    def set_window_icon(self):
        """设置窗口图标"""
        # 图标文件路径（与脚本同目录）
        icon_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "app_icon.ico")
        # 检查图标文件是否存在
        if os.path.exists(icon_path):
            self.setWindowIcon(QIcon(icon_path))
        else:
            print(f"警告：未找到图标文件 {icon_path}，将使用默认图标")

    def select_directory(self):
        """选择目录并填充到输入框"""
        dir_path = QFileDialog.getExistingDirectory(self, "选择待处理根目录")
        if dir_path:
            self.dir_input.setText(dir_path)

# 在 RenameMainWindow 类中修改以下方法：

    def open_config(self):
        """打开程序同级目录下的 config.yaml（修复变量作用域问题）"""
        # 定义默认配置内容（提前定义，确保所有分支都能访问）
        default_config = """
秘密:
    - 图纸
机密:
    - 实验计划
一般:
    - 日程表
"""
    
        # 获取程序（.py 或 .exe）所在目录
        if getattr(sys, 'frozen', False):
            # 打包后的 EXE 环境
            program_dir = os.path.dirname(sys.executable)
        else:
            # 未打包的脚本环境
            program_dir = os.path.dirname(os.path.abspath(__file__))
    
        # 配置文件路径（程序同级目录）
        config_path = os.path.join(program_dir, "config.yaml")
    
        # 若配置文件不存在，创建默认内容
        if not os.path.exists(config_path):
            try:
                with open(config_path, 'w', encoding='utf-8') as f:
                    f.write(default_config)  # 此时变量已提前定义，可正常访问
                # 显示创建成功的提示（注意：UI中无log_signal，改用QMessageBox）
                QMessageBox.information(self, "配置文件创建", f"已在程序目录创建默认配置文件：\n{config_path}")
            except Exception as e:
                QMessageBox.warning(self, "创建失败", f"无法创建配置文件：{str(e)}")
                return
    
        # 用系统默认程序打开配置文件
        try:
            if sys.platform == 'win32':
                os.startfile(config_path)
            else:
                subprocess.call(['open' if sys.platform == 'darwin' else 'xdg-open', config_path])
        except Exception as e:
            QMessageBox.warning(self, "打开失败", f"无法打开配置文件：{str(e)}")

    def start_process(self):
        """验证输入并启动后台处理"""
        root_dir = self.dir_input.text().strip()
        
        # 输入验证
        if not root_dir:
            QMessageBox.warning(self, "输入错误", "请输入待处理的根目录路径！")
            return
        if not os.path.isdir(root_dir):
            QMessageBox.warning(self, "路径错误", "指定的路径不存在或不是有效的目录！")
            return
        
        # 清空之前的显示内容
        self.stat_display.clear()
        self.modified_display.clear()
        self.unmodified_display.clear()
        
        # 禁用按钮防止重复点击
        self.process_btn.setDisabled(True)
        self.config_btn.setDisabled(True)
        self.select_dir_btn.setDisabled(True)
        
        # 启动后台线程
        self.rename_thread = RenameThread(root_dir)
        self.rename_thread.log_signal.connect(self.update_log)
        self.rename_thread.stat_signal.connect(self.update_statistics)
        self.rename_thread.finish_signal.connect(self.process_finish)
        self.rename_thread.start()

    def update_log(self, log_msg):
        """更新日志（这里暂用统计框显示实时日志，可根据需求调整）"""
        current_text = self.stat_display.toPlainText()
        new_text = current_text + (log_msg + "\n" if current_text else log_msg)
        self.stat_display.setPlainText(new_text)
        # 自动滚动到底部
        self.stat_display.verticalScrollBar().setValue(self.stat_display.verticalScrollBar().maximum())

    def update_statistics(self, total, modified, unmodified):
        """更新统计信息和文件列表显示"""
        # 1. 统计信息
        stat_text = f"""📊 处理统计
==============
总扫描文件数：{total}
已修改文件数：{modified}
未修改文件数：{len(unmodified)}
"""
        self.stat_display.setPlainText(stat_text)

        # 2. 已修改文件列表
        modified_text = "✅ 已修改文件\n" + "="*30 + "\n"
        if self.rename_thread.modified_paths:
            modified_text += "\n".join(self.rename_thread.modified_paths)
        else:
            modified_text += "无"
        self.modified_display.setPlainText(modified_text)

        # 3. 未修改文件列表
        unmodified_text = "❌ 未修改文件\n" + "="*30 + "\n"
        if unmodified:
            unmodified_text += "\n".join(unmodified)
        else:
            unmodified_text += "无"
        self.unmodified_display.setPlainText(unmodified_text)

    def process_finish(self):
        """处理完成后启用按钮"""
        self.process_btn.setDisabled(False)
        self.config_btn.setDisabled(False)
        self.select_dir_btn.setDisabled(False)
        QMessageBox.information(self, "处理完成", "所有文件处理已结束！详情请查看下方显示区域。")


# -------------------------- 程序入口 --------------------------
if __name__ == "__main__":
    app = QApplication(sys.argv)
    # 设置全局字体（避免中文乱码）
    font = QFont("Microsoft YaHei", 10)
    app.setFont(font)
    # 2. 关联应用全局图标（同时影响窗口、任务栏）
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, "app_icon.ico")
    if os.path.exists(icon_path):
        app_icon = QIcon(icon_path)
        # 同时设置应用图标和窗口图标（双重保障）
        app.setWindowIcon(app_icon)
        # 显式为任务栏设置图标（针对Windows系统）
        if sys.platform == 'win32':
            import ctypes
            # 加载Windows API，设置任务栏图标
            myappid = 'file.renamer.tool.v1.0'  # 自定义唯一ID（任意字符串）
            ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)
    else:
        print(f"警告：图标文件不存在 → {icon_path}")
    # 启动主窗口
    window = RenameMainWindow()
    window.show()
    sys.exit(app.exec())