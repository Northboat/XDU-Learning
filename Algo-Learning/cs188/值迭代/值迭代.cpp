#include <iostream>
using namespace std;
#include <iomanip>

#define LEFT 0
#define RIGHT 3
#define TOP 0
#define BOTTOM 2

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

Node graph[3][4];

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

//设置退出点和墙体 
void setEnd(int row, int colume, double val){
	graph[row][colume].maxVal = val;
	graph[row][colume].end = true;
	graph[row][colume].decision = "无";
}

//初始化地图 
void initGraph(){
	//墙体 
	setEnd(1, 1, 0);
	//得分点 
	setEnd(0, 3, 1);
	//失分点 
	setEnd(1, 3, -1);
}


int count = 0;
int times = 0;
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

//打印统计 
void printStatistics(){
	cout << "已迭代: " << ++times << "次\t" << "共递归: " << count << "次\n";
}

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