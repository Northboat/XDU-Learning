#include <iostream>
using namespace std;
#include <vector>
#include <set>

class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
        int m = matrix.size();
        if(m == 0){
            return;
        }
        int n = matrix[0].size();
        set<int> rows, columes;
        for(int index = 0; index < m*n; index++){
            if(matrix[index/n][index%n] == 0){
                rows.insert(index/n);
                columes.insert(index%n);
            }
        }
        for(auto row: rows){
            for(int i = 0; i < n; i++){
                matrix[row][i] = 0;
            }
        }
        for(auto colume: columes){
            for(int i = 0; i < m; i++){
                matrix[i][colume] = 0;
            }
        }
    }
};