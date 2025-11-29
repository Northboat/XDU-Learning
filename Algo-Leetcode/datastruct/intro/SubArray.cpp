#include <iostream>
using namespace std;

#include <vector>

class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int res = INT32_MIN;
        int sum = 0;
        for(vector<int>::iterator it = nums.begin(); it != nums.end(); it++){
            sum += *it;
            if(sum > res){
                res = sum;
            }
            if(sum < 0){
                sum = 0;
            }
        }
        return res;
    }
};

int main(){
    Solution s;
    vector<int> nums;
    for(int i = 0; i < 5; i++){
        nums.push_back(i);
    }
    cout << s.maxSubArray(nums) << endl;

}