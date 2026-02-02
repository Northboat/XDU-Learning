#include <iostream>
using namespace std;

#include <string>
#include <map>

class Solution {
public:
    bool wordPattern(string pattern, string s) {
        map<char, string> m;
        int n = s.length();
        int index = 0;
        for(int i = 0; i < n; i++){
            int j = i+1;
            char cur = pattern[index];
            while(j < n && s[j] != ' '){
                j++;
            }
            string temp = s.substr(i, j-i);
            cout << j << "    " << temp << endl;
            if(m.count(cur) && m[cur] != temp){
                cout << cur << " : " << temp << endl;
                return false;
            }
            m[cur++] = temp;
            index++;
            i = j;
        }
        if(index != pattern.length()){
            return false;
        }
        return true;
    }
};

int main(){
    Solution s;
    cout << s.wordPattern("abba", "dog cat cat dog");
    string str = "nmsl";
    //cout << str.substr(1,2) << endl;
}