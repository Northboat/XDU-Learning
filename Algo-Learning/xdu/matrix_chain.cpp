#include <iostream>
#include <vector>
#include <climits>
using namespace std;

// Function for Matrix Chain Multiplication using Dynamic Programming
int matrixChainDP(const vector<int>& dims) {
    int n = dims.size() - 1;
    vector<vector<int>> dp(n, vector<int>(n, 0));

    for (int len = 2; len <= n; ++len) {
        for (int i = 0; i < n - len + 1; ++i) {
            int j = i + len - 1;
            dp[i][j] = INT_MAX;
            for (int k = i; k < j; ++k) {
                int cost = dp[i][k] + dp[k + 1][j] + dims[i] * dims[k + 1] * dims[j + 1];
                dp[i][j] = min(dp[i][j], cost);
            }
        }
    }
    return dp[0][n - 1];
}

// Function for Matrix Chain Multiplication using Greedy Algorithm
int matrixChainGreedy(const vector<int>& dims) {
    vector<int> matrices = dims;
    int totalCost = 0;

    while (matrices.size() > 2) {
        int maxIndex = 1;
        for (int i = 1; i < matrices.size() - 1; ++i) {
            if (matrices[i] > matrices[maxIndex]) {
                maxIndex = i;
            }
        }

        int cost = matrices[maxIndex - 1] * matrices[maxIndex] * matrices[maxIndex + 1];
        totalCost += cost;

        // Remove the maximum dimension by merging the matrices
        matrices[maxIndex - 1] = matrices[maxIndex - 1];
        matrices.erase(matrices.begin() + maxIndex);
    }

    return totalCost;
}

int main() {
    vector<int> dims = {10, 20, 30, 40, 30}; // A1 = 10x30, A2 = 30x5, A3 = 5x60
    cout << "各矩阵维度: ";
	for(auto d: dims){
		cout << d << " ";
	}
	cout << endl;

    cout << "\n动态规划结果: ";
    int dpResult = matrixChainDP(dims);
    cout << dpResult << endl;

    cout << "\n贪心算法结果: ";
    int greedyResult = matrixChainGreedy(dims);
    cout << greedyResult << endl;

    return 0;
}

