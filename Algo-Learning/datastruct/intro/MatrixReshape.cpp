#include <iostream>
using namespace std;
#include <vector>

class Solution {
public:
    vector<vector<int>> matrixReshape1(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size();
        if(m == 0){
            return {};
        }
        int n = mat[0].size();
        if(m*n != r*c){
            return mat;
        }
        vector<int> vals;
        for(int i = 0; i < m; i++){
            for(int j = 0; j < n; j++){
                vals.push_back(mat[i][j]);
            }
        }
        vector<vector<int>> matrix;
        int index = 0;
        for(int i = 0; i < r; i++){
            vector<int> row;
            for(int j = 0; j < c; j++){
                row.push_back(vals[index++]);
            }
            matrix.push_back(row);
        }
        return matrix;
    }

    vector<vector<int>> matrixReshape(vector<vector<int>>& mat, int r, int c) {
        int m = mat.size();
        if(m == 0){
            return {};
        }
        int n = mat[0].size();
        if(m*n != r*c){
            return mat;
        }
        vector<vector<int>> matrix (r, vector<int> (c));
        for(int i = 0; i < m*n; i++){
            matrix[i/c][i%c] = mat[i/n][i%n];
        }
        return matrix;
    }
};

int main(){
    int r = 4;
    vector<vector<int>> matrix (r, vector<int> (1));
    cout << matrix[0].size();
}