#include <iostream>
using namespace std;
#include <vector>
#include<map>
#include<string>

class Solution {
public:
    vector<string> findRepeatedDnaSequences(string s) {
        map<string, int> used;
        int n = s.length();
        vector<string> res;
        for(int i = 0; i <= n-10; i++){
            string cur = s.substr(i, 10);
            cout << cur << endl;
            if(used.count(cur)){
                if(used[cur] == 1){
                    res.push_back(cur);
                }
                used[cur]++;
            } else {
                used[cur] = 1;
            }          
        }
        cout << "end" << endl;
        return res;
    }
};

int main(){
    Solution s;
    for(string str: s.findRepeatedDnaSequences("AAAAAAAAAAAAA")){
        cout << str << endl;
    }

}