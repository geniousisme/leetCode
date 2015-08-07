class Solution {
public:
    int minPathSum(vector<vector<int> >& grid) {
        int rowNum = grid.size(), colNum = grid[0].size();
        for (int i = 1; i < rowNum; i++) {
             grid[i][0] += grid[i - 1][0];
        };
        for (int j = 1; j < colNum; j++) {
             grid[0][j] += grid[0][j - 1];
        };
        for (int i = 1; i < rowNum; i++) {
             for (int j = 1; j < colNum; j++) {
                  grid[i][j] += grid[i - 1][j] > grid[i][j - 1] ? grid[i][j - 1] : grid[i - 1][j];
             };
        };
        return grid[rowNum - 1][colNum - 1];
    }
};