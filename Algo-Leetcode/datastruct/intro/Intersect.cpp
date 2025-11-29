#include <iostream>
using namespace std;

#include <vector>
#include <set>
#include <map>

class Solution {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        map<int, int> m;
        vector<int> res;
        for(int i = 0; i < nums1.size(); i++){
            if(m.count(nums1[i]) == 0){
                m.insert(pair<int, int> (nums1[i], 1));
                continue;
            }
            m[nums1[i]] = m[nums1[i]] + 1;
        }
        for(int i = 0; i < nums2.size(); i++){
            if(m.count(nums2[i]) != 0 && m[nums2[i]] > 0){
                res.push_back(nums2[i]);
                m[nums2[i]] = m[nums2[i]] - 1;
            }
        }
        return res;
    }
};

int main(){
    Solution s;
    vector<int> nums1 = {1,2,2,1};
    vector<int> nums2 = {2,2};
    vector<int> res = s.intersect(nums1, nums2);
    for(int i = 0; i < res.size(); i++){
        cout << res[i] << endl;
    }
    // map<int, int> m;
    // m[0] = 2;
    // cout << m.find(0)->second-1;
    // m.insert(pair<int,int>(0, m.find(0)->second-1));
    // cout << "hahaha: " << m[0] << endl; 
}