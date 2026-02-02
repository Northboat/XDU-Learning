#include <iostream>
using namespace std;

#include <vector>

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        int profit = 0;
        int minPrice = INT32_MAX;
        for(auto price: prices){
            profit = max(profit, price-minPrice);
            minPrice = min(minPrice, price);
        }
        return profit;
    }
};
