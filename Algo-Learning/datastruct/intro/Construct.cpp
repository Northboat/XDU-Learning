#include <iostream>
using namespace std;

#include <string.h>
#include <map>

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
        map<char, int> m;
        for(int i = 0; i < ransomNote.size(); i++){
            if(m.count(ransomNote[i]) == 0){
                m.insert(pair<char, int> (ransomNote[i], 1));
            } else {
                m[ransomNote[i]] = m[ransomNote[i]]+1;
            }
        }
        for(int i = 0; i < magazine.size(); i++){
            if(m.count(magazine[i]) != 0){
                m[magazine[i]] = m[magazine[i]]-1;
            }
        }
        map<char, int>::iterator it;
        for(it = m.begin(); it != m.end(); it++){
            cout << it->first << " " << it->second << endl;
            if(it->second > 0){
                return false;
            }
        }
        return true;
    }
};

int main(){
    Solution s;
    string r = "aa", m = "ab";
    cout << s.canConstruct(r, m);
}