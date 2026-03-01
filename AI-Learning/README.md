---
title: 经典人工智能算法实现
date: 2022-4-24
permalink: /pages/99e92c/
author: 
  name: Northboat
  link: https://github.com/Northboat
---

## 极大极小搜索的井字棋

Tic-Tac-Toe

- MinimaxSearch算法
- C语言实现

最深只有 9 层：has been solved

不得不说这是一个无聊的游戏：先落子者随便下不会输，后落子者占据中心后随便下不会输

### 极大极小搜索

极小极大搜索

~~~c
//极小极大搜索
int minimaxSearch(int depth){	//传入当前深度
	int value = 0;
	//初始化value，man最差情况为min 
	if (player == MAN) value = INT_MIN;
	//初始化ai value，最差情况为max 
	if (player == AI) value = INT_MAX;
	//如果游戏结束或深度耗尽，直接返回估值
	if (isEnd() != 0 || depth == MAXDEPTH){
		return evaluate();
	}

	for (int i = 0; i < ROW; i++){
		for (int j = 0; j < COL; j++){
			//遍历可以落子的点
			//planing过程，假设落子，扩展下一层搜索 
			if (board[i][j] == 0){
				//若当前为man落子
				if (player == MAN){
					//落子当前空位，判定空位已被占 
					board[i][j] = MAN;
					//切换选手 
					player = AI;
					//递归调用
					int nextValue = minimaxSearch(depth + 1);
					//切回当前选手 
					player = MAN;
					//此时落子手为人，为max节点，要求下一值大于当前值继续行动 
					if (value < nextValue){
						value = nextValue;
						if (depth == curDepth){
							bestPos.x = i;
							bestPos.y = j;
						}
					}
				}else if (player == AI){	//若当前为ai落子
					board[i][j] = AI;
					//切换选手 
					player = MAN;
					int nextValue = minimaxSearch(depth + 1);
					player = AI;
					//此时落子手为ai，为min节点，要求下一值小于当前值继续行动 
					if (value > nextValue){
						value = nextValue;
						if (depth == curDepth){
							bestPos.x = i;
							bestPos.y = j;
						}
					}
				}
				//重置ij状态，寻找下一空位 
				board[i][j] = 0;
			}
		}
	}
	//返回本层值，人赢为极大值，ai赢为极小值 
	return value;
}
~~~

评估方法

~~~c
//评估方法
int evaluate(){
	//isEnd判断是谁赢了，1则人，0则平，-1则ai 
	//MAN=1, AI=-1
	int value = isEnd();
	//若人赢了，返回最大值 
	if (value == MAN) return INT_MAX;
	//若AI赢了返回最小值 
	if (value == AI) return INT_MIN;
	//否则返回0，即和棋 
	return value;
}
~~~

### 功能实现

选手落子

~~~c
//ai落子 
void ai_play(){
	minimaxSearch(curDepth);
	board[bestPos.x][bestPos.y] = AI;
	curDepth++;
	player = MAN;
}

//玩家落子
void man_play(int x, int y){
	board[x][y] = MAN;
	curDepth++;
	player = AI;
}
~~~

输入函数

一个回合，人先落子，ai跟着落子

~~~c
//输入坐标
bool drop(){
	while(true){
		char c = _getch();
		if (!gameover){
			if (c >= '1' && c <= '9'){
				int posNum = c - '1';
				if(isFilled(posNum)){
					cout << "该点已经落子, 请重新选择\n\n";
					continue;
				}
				int x = posNum / 3;
				int y = posNum % 3;
				man_play(x, y);
				if (isEnd() == 0 && curDepth <= 8){
					ai_play();
					//cout << curDepth << endl;
                      //当ai落子后深度达到9说明游戏已结束，但有可能未分胜负
					if (isEnd() != 0 || curDepth == MAXDEPTH){
						//cout << "hahaha";
						gameover = true;
					}
				}else{
					//cout << "hahaha";
					gameover = true;
				}
				return false;
			}
		}else{
			if (c == 'r' || c == 'R'){
				init();
				return false;
			}
			return true;
		}
		if (c == 'q' || c == 'Q'){
			return true;
		}
		cout << "\n输入不合规范, 请重新输入, 若想退出程序请输入Q\n";
	}
}
~~~

判断功能

1️⃣ 判断是否落子

~~~c
//判断该点是否落子
bool isFilled(int pos){
	int x = pos / 3;
	int y = pos % 3;
	if(board[x][y] != 0){
		return true;
	}
	return false;
}
~~~

2️⃣ 判断游戏是否结束

~~~c
//判断是否结束，即有没有三个连着的同方落子，并返回count/3
//ai填充的是-1，man填充的是1，若以ai结束（ai胜利），将返回-1；若以man结束，则返回1
//若游戏未结束，返回0
int isEnd(){
	int i, j;
	int count;
	for (i = 0; i < ROW; i++){   //检查横着的每行是否有三个连着 
		count = 0;
		for (j = 0; j < COL; j++)
			count += board[i][j];
		if (count == 3 || count == -3)
			return count / 3;
	}
	for (j = 0; j < COL; j++){   //检查竖着的每列是否有三个连着 
		count = 0;
		for (i = 0; i < ROW; i++){
			count += board[i][j];
		}
		if (count == 3 || count == -3){
			return count / 3;
		}	
	}
	
	//检查两个对角线是否三个连着 
	count = board[0][0] + board[1][1] + board[2][2];
	if (count == 3 || count == -3){
		return count / 3;
	}
		
	count = board[0][2] + board[1][1] + board[2][0];
	if (count == 3 || count == -3){
		return count / 3;
	}	
	return 0;
}
~~~

3️⃣ 判断获胜信息，并打印显示

~~~c
//判断获胜信息 
void win(){
	if (gameover){
		if (isEnd() == MAN){
			cout << "游戏结束, 玩家胜利!\n\n";
		}else if (isEnd() == AI){
			cout << "游戏结束, 电脑胜利捏\n\n";
		}else{
			cout << "游戏结束, 平局\n\n";
		}
		cout << "按R键重开, 按任意键退出游戏\n\n游戏结果\n";
	}
}
~~~

初始化

~~~c
//玩家编号
#define MAN 1
#define AI -1

//搜索深度
#define MAXDEPTH 9

//棋盘行列
#define ROW 3
#define COL 3

//棋盘
int board[3][3] = {{0,0,0}, {0,0,0}, {0,0,0}};
//默认玩家先手
int player;
//当前最佳落子位置 
Pos bestPos;
//当前搜索深度
int curDepth;
//游戏是否结束
bool gameover;

//初始化游戏：棋盘、先行玩家、搜索深度(0)、游戏是否结束(false)
void init(){
	cout << "准备初始化棋盘，在任意过程中按 Q/q 可退出程序\n使用数字 1-9 选择落子方位，按从左往右从上往下的顺序递增\n如左上角为 1，中间为 5，右下角为 9\n";
	for (int i = 0; i < COL; i++){
		for (int j = 0; j < ROW; j++){
			board[i][j] = 0;
		}
	}
	//谁先走并设置搜索深度
	if(ai_first()){
         //若ai先手，深度+1
		curDepth = 1;
	}else{
		curDepth = 0;
	}
	//切换玩家落子
	player = MAN;
	//游戏未结束
	gameover = false;
	
}
~~~

~~~c
bool ai_first(){	
	cout << "\nAI先行? y/n\n\n";
	while(true){
		char c = _getch();
		if(c == 'y' || c=='Y'){
			ai_play();
			cout << "\n棋局开始，请落子\n";
			return true;
		}
		if(c == 'n' || c == 'N'){
			cout << "\n棋局开始，请落子\n";
			return false;
		}
		cout << "未能识别的字符\n";
	}
	
} 
~~~

打印棋盘

~~~c
//打印棋盘，玩家为 O，ai为X
void printBoard(){
	int i, j;
	for (i = 0; i < ROW; i++){
		cout << "-------------\n";
		for (j = 0; j < COL; j++){
			if (board[i][j] == AI){
				cout << "| X ";
			}else if (board[i][j] == MAN){
				cout << "| O ";
			}else{
				cout << "|   ";
			}
		}
		cout << "|\n";
	}
	cout << "-------------\n";
}
~~~

### 完整代码

[Bears-Experiment/Algo-Experiment/cs188/极小极大搜索 at main · Arkrypto/Bears-Experiment](https://github.com/Arkrypto/Bears-Experiment/tree/main/Algo-Experiment/cs188/极小极大搜索)

## 网格世界中的值迭代

> 网格世界

在一个4x3的二维数组中，存在墙体和退出点

|           |          |      |   +1   |
| :-------: | :------: | ---- | :----: |
|           | **墙体** |      | **-1** |
| **Start** |          |      |        |

在每个空格上，智能代理可以选择上下左右四个方向移动，但并不是严格执行，如

- 发出向上移动指令时，有10%概率向左移动，10%概率向右移动，80%概率向上移动
- 发出向左移动指令时，有10%概率向上移动，10%概率向下移动，80%概率向左移动

当碰到墙体或边界，奖励为0，请根据退出点做出每个空格上的最佳决策并返回各点奖励

贝尔曼方程
$$
V^*(s)=maxQ^*(s,a)\\Q^*(s,a)=avg(\sum(R(s,a,s')+\lambda V^*(s')))
$$
一个迭代的过程，直到找到退出条件向前进行值迭代，完善整个网格

### 辅助函数

初始化节点结构体

- maxVal：最大价值
- decision：最佳决策
- vals：上下左右四个Q-Value
- visited：是否被访问
- end：是否是墙体或退出点

~~~c
struct Node{
	//当前状态最大奖励
	double maxVal;
	//当前状态最佳决策 
	string decision;
	//当前状态分别向 上、下、左、右所获奖励 
	double vals[4];
	//是否被访问 
	bool visited;
	//是否是墙体或退出点 
	bool end;
};
~~~

初始化边界、图以及统计变量

- count：记录递归次数
- times：记录迭代次数

~~~c
#define LEFT 0
#define RIGHT 3
#define TOP 0
#define BOTTOM 2

Node graph[3][4];
int count = 0;
int times = 0;
~~~

初始化地图

~~~c
//初始化地图 
void initGraph(){
	//墙体 
	setEnd(1, 1, 0);
	//得分点 
	setEnd(0, 3, 1);
	//失分点 
	setEnd(1, 3, -1);
}
~~~

设置函数，设置退出点或墙体

~~~c
//设置退出点和墙体 
void setEnd(int row, int colume, double val){
	graph[row][colume].maxVal = val;
	graph[row][colume].end = true;
	graph[row][colume].decision = "无";
}
~~~

设置节点最佳策略

~~~c
//根据Q值设置最佳策略 
void setDecision(){
	for(int i = TOP; i <= BOTTOM; i++){
		for(int j = LEFT; j <= RIGHT; j++){
			for(int k = 0; k < 4; k++){
				if(graph[i][j].vals[k] == graph[i][j].maxVal && graph[i][j].maxVal != 0){
					switch(k){
						case 0: graph[i][j].decision = "上"; break;
						case 1: graph[i][j].decision = "下"; break;
						case 2: graph[i][j].decision = "左"; break;
						case 3: graph[i][j].decision = "右"; break; 
					}
					break;
				}
			}
		}
	}
	
}
~~~

设置节点最大价值

~~~c
//Q值设置当前状态最大奖励 
void setMaxVal(int row, int colume){

	for(int i = 0; i < 4; i++){
		if(graph[row][colume].vals[i] > graph[row][colume].maxVal){
			graph[row][colume].maxVal = graph[row][colume].vals[i];
		}
	}
//	if(row == 2 && colume == 3){
//		cout << "hahaha\n";
//	}
	
}
~~~

打印函数，打印地图

~~~c
//打印地图 
void printGraph(){
	cout << "\n----------------------------------------\n";
	for(int i = TOP; i <= BOTTOM; i++){
		for(int j = LEFT; j <= RIGHT; j++){
//			for(int k = 0; k < 4; k++){
//				cout << graph[i][j].vals[k] << "\t";
//			}
			cout << fixed << setprecision(4) << graph[i][j].maxVal;
			cout << " " << graph[i][j].decision << "|";
		}
		cout << "\n----------------------------------------\n";
	}
}

~~~

打印统计值

~~~c
//打印统计 
void printStatistics(){
	cout << "已迭代: " << ++times << "次\t" << "共递归: " << count << "次\n";
}
~~~

刷新访问状态

~~~c
//刷新被访问状态 
void flushGraph(){
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 4; j++){
			graph[i][j].visited = false;
		}
	}
	//根据当前Q(S,A)设置最佳策略 
	setDecision();
	//打印地图 
	printGraph();
	//打印统计 
	printStatistics();
}
~~~

### 值迭代

值迭代函数

~~~c
//值迭代函数 
double value_iterate(int row, int colume){
	count++;
	//当碰到边界，直接返回0 
	if(row < TOP || row > BOTTOM || colume < LEFT || colume > RIGHT){
		return 0;
	}
	
	//当节点已经被访问过，说明已经赋值了，于是返回最大值 
	//或当碰到墙体或退出点，直接返回 
	if(graph[row][colume].visited || graph[row][colume].end){
		return graph[row][colume].maxVal;
	}
	
	graph[row][colume].visited = true;

	//向上递归 
	graph[row][colume].vals[0] = 0.9*(0.8*value_iterate(row-1,colume) + 0.1*value_iterate(row,colume-1) + 0.1*value_iterate(row,colume+1));
	
	//向下递归 
	graph[row][colume].vals[1] = 0.9*(0.8*value_iterate(row+1,colume) + 0.1*value_iterate(row,colume-1) + 0.1*value_iterate(row,colume+1));
	
	//向左递归 
	graph[row][colume].vals[2] = 0.9*(0.8*value_iterate(row,colume-1) + 0.1*value_iterate(row+1,colume) + 0.1*value_iterate(row-1,colume));
	
	//向右递归 
	graph[row][colume].vals[3] = 0.9*(0.8*value_iterate(row,colume+1) + 0.1*value_iterate(row+1,colume) + 0.1*value_iterate(row-1,colume));
	
	//设置最佳策略、最大奖励、标记已访问 
	setMaxVal(row, colume);
	
	//cout << "已递归" << count << "次\n";
	
	return graph[row][colume].maxVal;
	
}
~~~

main函数

- 记录上一轮起点的最大价值，在下一轮与新值比较，若相同则说明迭代完成，退出循环；若不同则继续迭代

~~~c
int main(){
	//设置起始点 
	int row = 1, colume = 0;
	//初始化地形：墙体和退出点 
	initGraph();
	//记录上一轮初始点值 
	double pre = graph[row][colume].maxVal;
	//开始迭代 
	while(1){	
		//从初识点开始一轮值迭代	
		value_iterate(row, colume);
		//刷新节点均为被访问，同时打印统计数据和地图 
		flushGraph();				
		//当迭代后值未变化，说明迭代完成，退出循环 
		if(graph[row][colume].maxVal == pre){
			break;
		}
		//否则将当前值赋给pre，进行下一轮迭代 
		pre = graph[row][colume].maxVal;
	}
	
	cout << "\n\n最终结果:";
	printGraph();
	

	return 0;
}
~~~

### 完整代码

[Bears-Experiment/Algo-Experiment/cs188/值迭代 at main · Arkrypto/Bears-Experiment](https://github.com/Arkrypto/Bears-Experiment/tree/main/Algo-Experiment/cs188/值迭代)

对于这样一个`3x4`的网格，概率精确到小数点后六位，使用值迭代函数需要递归两千一百多次，所有概率都趋于稳定，迭代21轮

## 网格世界中的 Q Learning

对于同样的网格，对各状态Q-Value进行**学习**
$$
Q(s,a)=(1-\alpha)Q(s,a)+\alpha(R(s')+\lambda maxQ(s',a'))
$$

- α：学习率
- λ：折损率
- `s'`为状态`s`经过`a`到达的次状态

什么意思呢，就是说当前状态`s`执行行动`a`到达状态`s'`的价值等于经验`Q(s,a)`的一部分和目的状态`s'`的回报加`s'`最大的`Q-Value`的一部分

- 每执行一次行动，都要乘以一个折损率
- 对于每一次更新，都按学习率进行，即经验和新知识按这一比率构成新的经验

要注意的是，这并不是一个递归的过程，只是在当前基础上选择一个策略，执行，并获得结果并更新罢了

同样使用布尔变量`visited`表示访问状态，每轮学习时优先访问奖赏最大的节点，有概率（`epsilon`）访问其他节点

- `epsilon greedy`

### 初始化

节点结构体

~~~c
#include <iostream>
using namespace std;
#include <iomanip>
#include <stdlib.h>
#include <time.h>
//图边界 
#define left 0
#define right 3
#define top 0
#define bottom 2
//学习率 
#define rate 0.5
//折损率 
#define discount 0.9
//随即率
#define epsilon 0.2 

struct Node{
	//当前状态奖励
	double reward;
	//当前状态最佳决策 
	string decision;
	//当前状态分别向 上、下、左、右所获奖励 
	double vals[4];
	//是否被访问 
	bool visited;
	//是否是墙体或退出点 
	bool end;
};

Node graph[3][4];
~~~

方位类

- move函数便于移动至下一访问节点

  对于参数 step

  - 0表示向上移动
  - 1表示向下移动
  - 2表示向左移动
  - 3表示向右移动

~~~c
class Pos{
public:
	int row;
	int colume;
	
	Pos(int r, int c){
		row = r;
		colume = c;
	}
	
	Pos move(int step){
		switch(step){
			case 0:{
				Pos p(row-1, colume);
				return p;
			} 
			case 1:{
			 	Pos p(row+1, colume);
				return p;
			}
			case 2:{
				Pos p(row, colume-1);
				return p;
			}
			case 3:{
				Pos p(row, colume+1);
				return p;
			} 
		}
	}
};
~~~

初始化地图并设置退出点和墙体

~~~c
//设置退出点和墙体 
void setEnd(Pos p, double val){
	graph[p.row][p.colume].reward = val;
	graph[p.row][p.colume].end = true;
	graph[p.row][p.colume].decision = "无";
}
~~~

~~~c
//初始化地图 
void initGraph(){
	Pos p1(1, 1);
	Pos p2(0, 3);
	Pos p3(1, 3);
	
	//墙体 
	setEnd(p1, 0);
	//得分点 
	setEnd(p2, 1);
	//失分点 
	setEnd(p3, -1);
}
~~~

### Q-Learning

`q-learning`其实很好实现，代工式就行了，主要是如何去选择下一步位置，这很关键

在当前节点`learning`后，继续在下一节点执行`q-learning`，这个节点的选取取决于附近节点的奖赏和随机概率

- 若抽中概率，在除去最大节点之外的可选区节点随机选一个作为下一访问节点

- count用于统计函数执行次数
- 如果学习到墙壁或退出点，该点下一步将推出，我这里处理为`if(node.end){ next = (-1,-1) }`即将下一步移到`(-1,-1)`，下一步必退出；另外将这样的点的`Q-Value`统一存储在`vals[0]`，因为他的`reward`和`q-value`是完全分开的

~~~c
int count = 0;
//Q-Learning 
//并非是递归过程，只是在向前探索罢了 
void q_learning(Pos p){
	count++;
	int row = p.row, colume = p.colume;
	//cout << row << "  " << colume << endl;
	//当碰到边界，直接返回0 
	if(row < top || row > bottom || colume < left || colume > right){
		return;
	}
	Node node = graph[row][colume];
	if(node.visited){
		return;
	}
	graph[row][colume].visited = true;
	//随机移动 
	int step = nextStep(p);
	//cout << step << endl;
	//下一步位置 
	Pos next = p.move(step);
	//当node为退出点，下一步置为(-1,-1)，maxQ接收这一坐标返回零 
	//同时下一次q-learning将超出边界直接退出 
	//将退出点的QValue存在val[0] 
	if(node.end){
		next = Pos(-1, -1);
		step = 0;
	}
	//cout << step << endl;
	graph[row][colume].vals[step] = (1-rate)*node.vals[step] + rate*(node.reward + discount*maxQ(next));

	q_learning(next);
}
~~~

下一步选取

返回下一步方位

- 0表示上，1表示下，2表示左，3表示右

~~~c
int nextStep(Pos p){
	int row = p.row, colume = p.colume;
	return maxR(row, colume);
}
~~~

选取当前位置附近的奖励最大的节点并返回，有一定随机概率返回的不是最大值，而是除最大值之外能到达的节点，避免陷于局部最大

- `epsilon greedy`

~~~c
int maxR(int row, int colume){
	int reward[4];
	
	if(row-1 < top){ reward[0] = -2; } 
	else if(graph[row-1][colume].visited){ reward[0] = -1; }
	else { reward[0] = graph[row-1][colume].reward; }
	
	if(row+1 > bottom){ reward[1] = -2; }
	else if(graph[row+1][colume].visited){ reward[1] = -1; }
	else { reward[1] = graph[row+1][colume].reward; }
	
	if(colume-1 < left){ reward[2] = -2; } 
	else if(graph[row][colume-1].visited){ reward[2] = -1; }
	else { reward[2] = graph[row][colume-1].reward; }
	
	if(colume+1 > right){ reward[3] = -2; }
	else if(graph[row][colume+1].visited){ reward[3] = -1; }
	else { reward[3] = graph[row][colume+1].reward; }
	
	//cout << r1 << " " << r2 << " "<< r3 << " "<< r4 << endl;
	int step = compare(reward[0], reward[1], reward[2], reward[3]);
	double random =  rand()%10 * 0.1;
	if(random <= epsilon){
		for(int i = 0; i < 4; i++){
			if(i != step && reward[i] != -2){
				step = i;
				break;
			}
		}
	}
	return step;
	
}
~~~

比较传入的四个值，根据大小返回最大值的下标

~~~c
int compare(int r1, int r2, int r3, int r4){
	//向上 
	if(r1 >= r2 && r1 >= r3 && r1 >= r4){ return 0; }
	//向右 
	if(r4 >= r1 && r4 >= r2 && r4 >= r3){ return 3; }
	//向下 
	if(r2 >= r1 && r2 >= r3 && r2 >= r4){ return 1; }
	//向左 
	if(r3 >= r1 && r3 >= r2 && r3 >= r4){ return 2;	}
	
}
~~~

根据当前节点`P`的`Q-Value`设置最佳策略

~~~c
void setDecision(Pos p, int index){
	int row = p.row, colume = p.colume;
	switch(index){
		case 0: graph[row][colume].decision = "上"; break;
		case 1: graph[row][colume].decision = "下"; break;
		case 2: graph[row][colume].decision = "左"; break;
		case 3: graph[row][colume].decision = "右"; break;
	}
} 

double maxQ(Pos p){
	int row = p.row, colume = p.colume;
	if(row == -1 && colume == -1){
		return 0;
	}
	Node node = graph[row][colume];
	if(node.end){
		return node.vals[0];
	}
	double max = 0;
	for(int i = 0; i < 4; i++){
		if(node.vals[i] > max){
			max = node.vals[i];
			if(!node.end)
				setDecision(p, i); 
		}
	}
	return max;
}
~~~

### 辅助函数

打印地图和刷新节点访问状态

~~~c
//打印图 
void printGraph(){
	cout << "\n----------------------------------------\n";
	for(int i = top; i <= bottom; i++){
		for(int j = left; j <= right; j++){
			Pos p(i, j);
			cout << fixed << setprecision(4) << maxQ(p);
			cout << " " << graph[i][j].decision << "|";
		}
		cout << "\n----------------------------------------\n";
	}
}

//刷新被访问状态 
void flushGraph(){
	for(int i = 0; i < 3; i++){
		for(int j = 0; j < 4; j++){
			graph[i][j].visited = false;
		}
	}
	//打印地图 
	printGraph();
}
~~~

#### 完整代码

[Bears-Experiment/Algo-Experiment/cs188/Q-Learning at main · Arkrypto/Bears-Experiment](https://github.com/Arkrypto/Bears-Experiment/tree/main/Algo-Experiment/cs188/Q-Learning)

相较于递归两千余次的值迭代，`q-learning`函数执行400余次后最佳策略已然可以得出并且不改变，执行1000余次后小数点后四位概率趋于稳定
