#include "include/common.h"

// Chris::NTR

class Solution {
public:
    int numTrees(int n) {
        if (n < 2){
            return 1;
        };
        vector<int> dp(n + 1, 0);
        dp[0] = 1; dp[1] = 1;
        for (int i = 2; i < dp.size(); i++) {
             dp[i] = catlan_result(dp, i - 1);
        };
        return dp[n];
    }
private:
    int catlan_result(vector<int>& dp, int index) {
        int start = 0, end = index, res = 0;
        while (end > -1){
               res += dp[start] * dp[end];
               start++; 
               end--;
        };
        return res;
    }
};

int main(void) {
    Solution s;
    cout << s.numTrees(1) << endl;
    cout << s.numTrees(2) << endl;
    cout << s.numTrees(3) << endl;
    cout << s.numTrees(4) << endl;
    cout << s.numTrees(5) << endl;
    return 0;
};