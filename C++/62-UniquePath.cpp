#include "include/common.h"

class Solution {
public:
    int uniquePaths(int m, int n) {
        vector< vector<int> > maze(m, vector<int> (n, 0));
        for (int i = 0; i < m; i++) {
             maze[i][0] = 1;
        };
        for (int j = 0; j < n; j++) {
             maze[0][j] = 1;
        };
        for (int i = 1; i < m; i++) {
             for (int j = 1; j < n; j++) {
                  maze[i][j] = maze[i - 1][j] + maze[i][j - 1];
             };
        };
        return maze[m - 1][n - 1];
    }
};

int main(void) {
    Solution s;
    cout << s.uniquePaths(3, 2) << endl;
    return 0;
};