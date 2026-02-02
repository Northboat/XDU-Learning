#include <iostream>
using namespace std;

// n 表示要加到的和，m 表示当前因子最大能达到的值
// 如 partition(5, 1) 表示用不大于 1 的正整数划分 5，只有一种 1+1+1+1+1
int partition(int n, int m) {
	// 当和为 1 或最大因子为 1，只有一种情形，一个一个加上去
	if (n == 1 || m == 1) {
		return 1;
	} else if (n == m) { // 当和与最大因子值相同，去掉 n = m，剩下 partition(n, m-1)
		return 1 + partition(n, m - 1);
	} else if (n < m) {
		return partition(n, n);
	}
	// 把当前因子最大值递减，依次参与构成 n
	// 把当前和减去 m，表示存在一个比 n 小的参数 m
	return partition(n, m - 1) + partition(n - m, m);
}

int partition(int n) {
	return partition(n, n);
}

int main() {
	cout << partition(5);
	return 0;
}
