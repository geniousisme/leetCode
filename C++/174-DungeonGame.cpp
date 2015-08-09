#include "include/common.h"

class Solution {
public:
    int calculateMinimumHP(vector<vector<int> >& dungeon) {
        int rowNum = dungeon.size(), colNum = dungeon[0].size(), min = 0;
        dungeon[rowNum - 1][colNum - 1] = dungeon[rowNum - 1][colNum - 1] > 0 ? 1 : 1 - dungeon[rowNum - 1][colNum - 1];
        for (int i = rowNum - 2; i > -1; i--) {
             dungeon[i][colNum - 1] = dungeon[i + 1][colNum - 1] - dungeon[i][colNum - 1] > 0 ? dungeon[i + 1][colNum - 1] - dungeon[i][colNum - 1] : 1;
        };
        for (int j = colNum - 2; j > -1; j--) {
             dungeon[rowNum - 1][j] = dungeon[rowNum - 1][j + 1] - dungeon[rowNum - 1][j] > 0 ? dungeon[rowNum - 1][j + 1] - dungeon[rowNum - 1][j] : 1; 
        };
        for (int i = rowNum - 2; i > -1; i--) {
             for (int j = colNum - 2; j > -1; j--) {
                  min = dungeon[i + 1][j] < dungeon[i][j + 1] ? dungeon[i + 1][j] : dungeon[i][j + 1];
                  dungeon[i][j] = min > dungeon[i][j] ? min - dungeon[i][j] : 1;
             };
        };
        return dungeon[0][0];
    }
};
int main(void) {
    Solution s;
    vector< vector<int> > test (3, vector<int>(3, 0));
    // test[0][0] = 0, test[0][1] = 5;
    // test[1][0] = -2, test[1][1] = -3;
    test[0][0] = -2, test[0][1] = -3, test[0][2] = 3;
    test[1][0] = -5, test[1][1] = -10, test[1][2] = 1;
    test[2][0] = 10, test[2][1] = 30, test[2][2] = -5;
    cout << s.calculateMinimumHP(test) << endl;
    return 0;
};
//  0,  5
// -2, -3