#include <string>
#include <vector>
#include <iostream>

class Solution {
public:
    int maxProfit(std::vector<int>& prices) {
        int max_profit = 0;
        for (int i = 1; i < prices.size(); i++){
            int diff = prices[i] - prices[i - 1];
            if (diff > 0)   max_profit += diff; 
        };
        return max_profit;
    }
};

int main(int argc, char *argv []){
    Solution s;
    int arr [] = {3,4,1,5,2,6};
    std::vector<int> iarr(arr, arr + 6);
    std::cout << "max profit: " << s.maxProfit(iarr) << std::endl;
    return 0;
};