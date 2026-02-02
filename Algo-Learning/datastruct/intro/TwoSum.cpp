#include <iostream>
using namespace std;

#include <map>
#include <vector>

class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        map<int, int> m;
        for(int i = 0; i < nums.size(); i++){
            if(m.count(target-nums[i]) == 1){
                return {i, m.at(target-nums[i])};
            }
            m.insert(pair<int, int>(nums[i], i));
        }
        return {};
    }
};

int main(){
    Solution s;
    map<int,int> m;
    m.insert(pair<int, int>(1, 2));
    m.insert(pair<int, int>(3,4));
    cout << m.at(5) << endl;
}