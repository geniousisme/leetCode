#include "include/common.h"

class Solution {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.empty()) {
            return 0;
        };
        int min = prices[0], maxProfit = 0;
        for(int i = 0; i < prices.size(); i++) {
            if (min > prices[i]) {
                min = prices[i];
            };
            if (maxProfit < prices[i] - min) {
                maxProfit = prices[i] - min;
            }
        };
        return maxProfit;
    }
};

int main(void) {
    Solution s;
    int arr [] = {4, 5, 2, 6, 9};
    vector<int> iarr(arr, arr + 5);
    cout << s.maxProfit(iarr) << endl;
    int arr1 [] = {9, 2};
    vector<int> iarr1(arr1, arr1 + 2);
    cout << s.maxProfit(iarr1) << endl;
    int arr2 [] = {9};
    vector<int> iarr2(arr2, arr2 + 1);
    cout << s.maxProfit(iarr2) << endl;
    return 0;
};