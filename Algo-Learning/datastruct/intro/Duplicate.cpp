#include <iostream>
using namespace std;

#include <vector>
#include <set>

class Solution {
public:
    bool containsDuplicate(vector<int>& nums) {
        set<int> s;
        vector<int>::iterator it;
        for(it = nums.begin(); it != nums.end(); it++){
            if(s.count(*it) == 0){
                s.insert(*it);
            } else {
                return true;
            }
        }
        return false;
    }
};

int main(){
    Solution s;
    vector<int> nums;
    nums.push_back(1);
    nums.push_back(2);
    nums.push_back(3);
    cout << s.containsDuplicate(nums) << endl;
}