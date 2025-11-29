#include <iostream>
using namespace std;
#include <vector>
#include <deque>

class Solution {
	public:
		int networkDelayTime(vector<vector<int>> &times, int n, int k) {
			vector<int> res(n + 1, INT_MAX);
			deque<int> queue;
			vector<int> visited(n + 1);

			queue.push_back(k);
			visited[k] = 1;
			res[k] = 0;
			while (!queue.empty()) {
				int cur = queue.front();
				queue.pop_front();
				vector<int> next = times[cur];
				for (int j = 0; j < (int)next.size(); j++) {
					if (next[j] == -1 || visited[j]) {
						continue;
					}
					queue.push_back(j);
					visited[j] = 1;
					res[j] = res[cur] + next[j];
				}
			}
			int max = 0;
			for (int i = 1; i <= n; i++) {
				if (res[i] > max) {
					max = res[i];
				}
			}
			return max == INT_MAX ? -1 : max;
		}
};

int main() {
	cout << "nmsl" << endl;
}