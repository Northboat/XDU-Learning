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

Node graph[3][4];



//设置退出点和墙体 
void setEnd(Pos p, double val){
	graph[p.row][p.colume].reward = val;
	graph[p.row][p.colume].end = true;
	graph[p.row][p.colume].decision = "无";
}

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

int nextStep(Pos p){
	int row = p.row, colume = p.colume;
	return maxR(row, colume);
}

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

int main(){
	//设置起始点 
	int row = 2, colume = 0;
	Pos p(row, colume);
	//初始化地形：墙体和退出点 
	initGraph();
	cout << graph[1][3].reward << endl;
	//记录上一轮初始点值 
	for(int i = 0; i < 100; i++){
		q_learning(p);
		flushGraph();
	}
	
	cout << "共学习" << count << "次" << endl;
	//printGraph();

	system("pause"); 
	return 0;
}