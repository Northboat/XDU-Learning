#include <iostream>
using namespace std;

class Solution {
public:

    int pick;

    Solution(int pick){
        this->pick = pick;
    }

    int guess(int num){
        if(pick > num){
            return 1;
        }
        if(pick < num){
            return -1;
        }
        return 0;
    }

    int guessNumber(int n) {
        int left = 1, right = n;
        // 以这种形式求中点，防止 left+right 溢出 integer
        int mid = left + (right-left) / 2;
        while(guess(mid) != 0){
            if(left >= right){
                cout << "nmsl" << endl;
                return -1;
            }
            //cout << left << "-" << right << " " << mid << " " << guess(mid) << endl;
            if(guess(mid) == 1) { left = mid+1; }
            else { right = mid-1; }
            mid = left + (right-left) / 2;
        }   
        return mid;
    }
};

int main(){
    Solution s(7);
    cout << s.guessNumber(10) << endl;
}