#include "include/common.h"

class Solution {
public:
    int numSquaresDP(int n) {
        vector<int> dp(n + 1, numeric_limits<int>::max());
        for (int i = 1; i * i <= n; i++) {
             dp[i * i] = 1;
        };
        for (int i = 1; i <= n; i++) {
             for (int j = 1; i + j * j <= n; j++) {
                  dp[i + j * j] = min(dp[i] + 1, dp[i + j * j]);
             };
        };
        return dp[n];
    }
};

int main(void) {
    Solution s;
    for (int i = 1; i <= 12; i++) {
         cout << i << ": " << s.numSquares(i) << endl;
    };
    return 0;
};