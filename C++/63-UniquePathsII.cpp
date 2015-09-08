#include "include/common.h"

class Solution {
public:
    int uniquePathsWithObstaclesI(vector<vector<int> >& obstacleGrid) {
        int rowNum = obstacleGrid.size(), colNum = obstacleGrid[0].size();
        if (obstacleGrid[0][0] || obstacleGrid[rowNum - 1][colNum - 1]) {
            return 0;
        };
        int obstacleFlag = 1;
        for (int i = 0; i < rowNum; i++) {
             if (obstacleGrid[i][0] == 1) {
                 obstacleFlag = 0;
             };
             obstacleGrid[i][0] = obstacleFlag;
        };
        obstacleFlag = 1;
        for (int j = 1; j < colNum; j++) {
             if (obstacleGrid[0][j] == 1) {
                 obstacleFlag = 0;
             };
             obstacleGrid[0][j] = obstacleFlag;
        };
        for (int i = 1; i < rowNum; i++) {
             for (int j = 1; j < colNum; j++) {
                  if (obstacleGrid[i][j] == 1) {
                      obstacleGrid[i][j] = 0;
                  }
                  else {
                      obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1];
                  }
             };
        };
        return obstacleGrid[rowNum - 1][colNum - 1];
    }
    int uniquePathsWithObstacles(vector<vector<int> >& obstacleGrid) {
        int rowNum = obstacleGrid.size(), colNum = obstacleGrid[0].size();
        if (obstacleGrid[0][0] == 1 || obstacleGrid[rowNum - 1][colNum - 1] == 1) {
            return 0;
        };
        obstacleInit(obstacleGrid, rowNum, colNum);
        for (int i = 1; i < rowNum; i++) {
             for (int j = 1; j < colNum; j++) {
                  if (obstacleGrid[i][j] == 1) {
                      obstacleGrid[i][j] = 0;
                  }
                  else {
                      obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1];
                  };
             };
        };
        return obstacleGrid[rowNum - 1][colNum - 1];
    }
private:
    int obstacleExist;
    void obstacleInit(vector<vector<int> >& maze, int rowNum, int colNum) {
         obstacleExist = 1;
         for (int j = 1; j < colNum; j++) {
              if (maze[0][j] == 1) {
                  obstacleExist = 0;
              };
              maze[0][j] = obstacleExist;
         };
         obstacleExist = 1;
         for (int i = 1; i < rowNum; i++) {
              if (maze[i][0] == 1) {
                  obstacleExist = 0;
              };
              maze[i][0] = obstacleExist;
         };
         return;
    }
};

int main(void) {
    Solution s;
    vector< vector<int> > test(3, vector<int>(3, 0));
    // test[1][0] = 1;
    cout << s.uniquePathsWithObstacles(test) << endl;
    vector< vector<int> > test2(1, vector<int>(1, 0));
    // test[0][0] = 1;
    cout << s.uniquePathsWithObstacles(test2) << endl;
    return 0;
};