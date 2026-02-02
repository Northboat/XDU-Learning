import os
import re
import yaml
import sys
from pathlib import Path
from datetime import datetime

# 全局统计变量
total_files = 0          # 总扫描文件数
modified_files = 0       # 已修改文件数
unmodified_files = []    # 未修改文件路径列表

def load_config(config_path):
    """加载并标准化配置文件"""
    try:
        with open(config_path, 'r', encoding='utf-8') as f:
            config = yaml.safe_load(f)
        
        if not isinstance(config, dict):
            raise ValueError("配置文件必须是字典格式（分组: 关键词列表）")
        
        normalized_config = {}
        for group, keywords in config.items():
            if not isinstance(keywords, list):
                keywords = [str(keywords).strip()]
            normalized_config[group] = [str(kw).strip() for kw in keywords if str(kw).strip()]
        
        return normalized_config
    
    except FileNotFoundError:
        log("错误：未找到 config.yaml 文件！")
        return None
    except Exception as e:
        log(f"配置文件错误：{str(e)}")
        return None

def log(message):
    """同时输出到控制台和日志文件"""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {message}\n"
    
    # 输出到控制台
    print(log_line.strip())
    
    # 写入日志文件
    with open("renamer.log", "a", encoding="utf-8") as f:
        f.write(log_line)

def remove_existing_prefix(filename):
    """移除已有的★分组名★前缀"""
    prefix_pattern = re.compile(r'^★.*?★')
    return prefix_pattern.sub('', filename)

def rename_in_directory(root_dir, config):
    """递归处理目录下所有文件，更新统计信息"""
    global total_files, modified_files, unmodified_files
    
    for entry in os.scandir(root_dir):
        if entry.is_dir(follow_symlinks=False):
            rename_in_directory(entry.path, config)
        elif entry.is_file():
            filename = entry.name
            file_path = entry.path
            
            # 跳过脚本自身和配置文件（不计入统计）
            if (filename == Path(__file__).stem + ".exe" and root_dir == os.getcwd()) or filename == "config.yaml":
                continue
            
            # 累计总文件数
            total_files += 1
            modified = False  # 标记是否被修改
            
            original_filename = remove_existing_prefix(filename)
            
            for group, keywords in config.items():
                for keyword in keywords:
                    if keyword in original_filename:
                        new_filename = f"★{group}★{original_filename}"
                        new_file_path = os.path.join(root_dir, new_filename)
                        
                        if new_file_path != file_path:
                            os.rename(file_path, new_file_path)
                            log(f"已更新：{file_path} → {new_file_path}")
                            modified = True
                            modified_files += 1
                        break
                else:
                    continue
                break
            
            # 记录未修改的文件
            if not modified:
                unmodified_files.append(file_path)

def print_statistics():
    """输出统计信息到日志"""
    log("===== 处理统计 =====")
    log(f"总扫描文件数：{total_files}")
    log(f"已修改文件数：{modified_files}")
    log(f"未修改文件数：{len(unmodified_files)}")
    
    if unmodified_files:
        log("未修改的文件路径：")
        for path in unmodified_files:
            log(f"- {path}")
    # log("====================")

if __name__ == "__main__":
    # 初始化日志（清空历史日志，可选）
    # with open("renamer.log", "w", encoding="utf-8") as f:
    #     f.write(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] 日志开始\n")
    
    # 提示用户输入根目录（支持默认值）
    print("请输入需要处理的根目录绝对路径（直接回车则使用当前目录）：")
    user_input = input().strip()  # 获取用户输入并去除首尾空格
    
    # 处理用户输入
    if user_input:
        root_directory = user_input
        # 检查路径是否存在
        if not os.path.isdir(root_directory):
            print(f"错误：指定的路径不存在或不是目录 → {root_directory}")
            input("按任意键退出...")
            sys.exit(1)
    else:
        # 用户未输入，使用当前目录
        root_directory = os.getcwd()
        print(f"将使用当前目录作为根目录：{root_directory}")

    config = load_config(os.path.join(root_directory, "config.yaml"))
    
    if config:
        log(f"开始处理根目录：{root_directory} 及其所有子目录")
        rename_in_directory(root_directory, config)
        print_statistics()  # 输出统计信息
        log("处理完成\n\n\n")
    else:
        log("配置加载失败，未执行任何操作")
    
    input("\n按任意键退出...")