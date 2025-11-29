#include <iostream>
using namespace std;

#include <string>

class Solution {
public:
    string multiply(string num1, string num2) {
        int m = num1.length(), n = num2.length();
        int ength = n>m?n:m;
        string res;

        for(int i = 1; i <= m; i++){
            string row;
            int cur = num1[m-i]-'0';
            int flag = 0;
            //cout << cur << endl;
            for(int j = 1; j <= n; j++){
                int fac = num2[n-j]-'0';
                int ans = cur * fac + flag;
                //cout << ans << endl;
                if(ans >= 10){
                    flag = ans/10;
                    ans = ans%10;  
                } else {
                    flag = 0;
                }
                //cout << ans << endl;
                row = to_string(ans) + row;
                //cout << row << endl;
            }
            if(flag){
                row = to_string(flag) + row;
            }
            for(int k = 1; k < i; k++){
                //cout << row << endl;
                row = row+"0";
            }
            if(i == 1){
                res = row;
            } else {
                res = addStrings(res, row);
            }
        }
        return res;
    }
    
    string addStrings(string num1, string num2) {
        int m = num1.size(), n = num2.size();
        int index = 1, flag = 0;
        int length = n>m ? n:m;
        string ans(length, ' ');
        while(index <= m && index <= n){
            int cur = (num1[m-index]-'0') + (num2[n-index]-'0');
            if(flag){
                cur++;
                flag = false;
            }
            if(cur >= 10){
                flag = true;
                ans[length-index] = (cur-10)+'0';
            } else {
                ans[length-index] = cur+'0';
            }
            index++;
        }
        while(index <= m){
            int cur = num1[m-index]-'0';
            if(flag){
                cur++;
                flag = false;
            }
            if(cur >= 10){
                flag = true;
                ans[length-index] = (cur-10)+'0';
            } else {
                ans[length-index] = cur+'0';
            }
            index++;
        }
        while(index <= n){
            int cur = num2[n-index]-'0';
            if(flag){
                cur++;
                flag = false;
            }
            if(cur >= 10){
                flag = true;
                ans[length-index] = (cur-10)+'0';
            } else {
                ans[length-index] = cur+'0';
            }
            index++;
        }
        if(flag){
            ans = "1" + ans;
        }
        return ans;
    }
};

int main(){
    Solution s;
    cout << s.multiply("2", "3") << endl;
}