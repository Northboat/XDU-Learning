#include <iostream>
using namespace std;

#include <string>
#include <map>
#include <vector>
#include <algorithm>

void printVec(vector<int> vec){
    for(auto it: vec){
        cout << it << ", ";
    }
    cout << endl;
}

class Solution {
public:
    vector<int> partitionLabels(string s) {
        map<char,vector<int>> m;
        for(int i = 0; i < s.length(); i++){
            char cur = s[i];
            if(m.count(cur)){
                m[cur][1] = i;
            } else {
                m[cur] = {i, i};
            }
        }
        vector<vector<int>> vec;
        for(auto v: m){
            vec.push_back(v.second);
        }
        sort(vec.begin(), vec.end());
        vector<vector<int>> merged;
        for(int i = 0; i < vec.size(); i++){
            vector<int> cur = vec[i];
            printVec(cur);
            if(merged.empty() || cur[0] > merged.back()[1]){
                merged.push_back(cur);
            }
            if(cur[1] > merged.back()[1]){
                merged.back()[1] = cur[1];
            }
        }
        vector<int> res;
        for(int i = 0; i < merged.size(); i++){
            res.push_back(merged[i][1]-merged[i][0]+1);
        }
        return res;
    }
};

int main(){
    Solution s;
    printVec(s.partitionLabels("ababcbacadefegdehijhklij"));
    
}