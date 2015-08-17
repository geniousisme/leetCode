#include "include/common.h"

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        };
        int max = prices[0], min = prices[0], profit = 0;
        for(int i = 1; i < prices.size(); i++) {
            if (prices[i] > max) {
                max = prices[i];
            };
            if(prices[i] < min) {
               min = prices[i];
            };
            profit = max - min;
        };
        return profit;
    }
};

int main(void) {
    Solution s;
    int arr [] = {4, 5, 2, 6, 9};
    vector<int> iarr(arr, arr + 5);
    cout << s.maxProfit(iarr) << endl;
    return 0;
};