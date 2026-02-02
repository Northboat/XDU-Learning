#include <iostream>
using namespace std;

#include <vector>

class Solution {
public:
    vector<vector<int>> generate(int numRows) {
        vector<vector<int>> matrix;
        for(int i = 0; i < numRows; i++){
            vector<int> row;
            for(int j = 0; j < i+1; j++){
                if(j == 0 || j==i) { row.push_back(1); continue; }
                row.push_back(matrix[i-1][j-1]+matrix[i-1][j]);
            }
            matrix.push_back(row);            
        }
        return matrix;
    }
};

int main(){
    Solution s;
    vector<vector<int>> m = s.generate(5);
    for(int i = 0; i < m.size(); i++){
        for(int j = 0; j < m[i].size(); j++){
            cout << m[i][j] << " ";
        }
        cout << endl;
    }
}