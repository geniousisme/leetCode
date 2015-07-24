#include "include/common.h"

class Solution {
public:
    int totalNQueens(int n) {
        for (int i = 0; i < n; i++) {
             board.push_back(-1);
        };
        // int res = 0;
        // totalQueensHelper(n, 0, res);
        // return res;
        return totalQueensHelperII(n);
    }
    void totalQueensHelper(int n, int column, int& res) {
         if (column == n) {
             res++;
             return;
         };
         for (int row = 0; row < n; row++) {
             if (queen_judge(column, row)) {
                 board[column] = row;
                 totalQueensHelper(n, column + 1, res);
             };
         };
    };
    int totalQueensHelperII(int n, int column = 0) {
        if (column == n) {
            return 1;
        };
        int res = 0;
        for (int row = 0; row < n; row++) {
             if (queen_judge(column, row)) {
                 board[column] = row;
                 res += totalQueensHelperII(n, column + 1);
             };
        };
        return res;
    };
private:
    vector<int> board;
    bool queen_judge(int column, int row) {
         for (int col = 0; col < column; col++) {
              if (board[col] == row || abs(col - column) == abs(board[col] - row)) {
                  return false;
              };
         };
         return true;
    }
};

int main(void) {
    Solution s;
    cout << s.totalNQueens(4) << endl;
    return 0;
}