#include "include/common.h"

class Solution {
public:
    int recClimbStairs(int n) {
        if (n == 1 || n == 0) {
            return 1;
        };
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
    int climbStairsI(int n) {
        vector<int> res(2, 1);
        if (n >= 2) {
            for (int i = 2; i <= n; i++) {
                 res.push_back(res[i - 1] + res[i - 2]);
            }
        };
        return res[n];
    }
    int climbStairs(int n) {
        if (n == 0 || n == 1) {
            return 1;
        };
        return climbStairs(n - 1) + climbStairs(n - 2);
    }
};

int main(void) {
    Solution s;
    for (int i = 0; i < 45; i++)  cout << s.climbStairs(i) << " ";
    cout << endl;
    return 0;
};

// 1 2 3 4
// 1 2 3 5