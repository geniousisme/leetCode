#include "include/common.h"

//Chris:NTR!!!!

class Solution {
public:
    vector< vector<string> > solveNQueens(int n) {
                             for (int i = 0; i < n; i ++) {
                                  board.push_back(-1);
                             };
                             queen_num = n;
                             vector< vector<string> > res;
                             vector<string> queenArr;
                             dfs(0, queenArr, res);
                             return res;   
    }
    void dfs(int column_num, vector<string>& queenArr, vector< vector<string> >& res) {
         if (column_num == queen_num) {
            res.push_back(queenArr);
            return;
         };
         for (int row = 0; row < queen_num; row++) {
              if (queen_judge(column_num, row)) {
                  board[column_num] = row;
                  string queenStr = "";
                  for (int i = 0; i < queen_num; i++){
                       queenStr += i == row ? "Q" : "."; 
                  };
                  queenArr.push_back(queenStr);
                  dfs(column_num + 1, queenArr, res);
                  queenArr.pop_back();
              };
         };

    }
private:
    vector<int> board;
    int queen_num;
    bool queen_judge(int column, int row) {
         for (int col = 0; col < column; col++) {
             if (board[col] == row || abs(col - column) == abs(board[col] - row)) {
                 return false;
             };
         };
         return true;
    };

};

int main(void) {
    Solution s;
    s.solveNQueens(4);
    return 0;
};