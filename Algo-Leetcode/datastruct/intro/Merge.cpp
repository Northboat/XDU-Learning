#include <iostream>
using namespace std;

#include <vector>

class Solution {
public:
    void merge(vector<int>& nums1, int m, vector<int>& nums2, int n) {
        int tail = m+n-1;
        int p1 = m-1, p2 = n-1;
        while(tail >=0){
            int cur;
            if(p1 < 0){
                cur = nums2[p2--];
            } else if(p2 < 0){
                cur = nums1[p1--];
            } else {
                cur = nums1[p1]>nums2[p2] ? nums1[p1--]:nums2[p2--];
            }
            nums1[tail--] = cur;
        }
    }
};

int main(){

    int a = 2;
    int b = 3;
    int c = a>b ? a--:b--;
    cout << a << endl << b << endl << c;
}