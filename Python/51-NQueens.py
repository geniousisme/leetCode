class Solution:
    # @param {integer} n
    # @return {string[][]}
    def solveNQueens(self, n):
        self.n = n
        self.board = [-1 for i in xrange(self.n)]
        res = []
        self.dfs(0, [], res)
        return res
    
    def dfs(self, col_num, queen_list, res):
        if col_num == self.n:
           res.append(queen_list)
           return
        for i in xrange(self.n):
            if self.queen_judge(col_num, i):
               self.board[col_num] = i
               queen_row = '.' * self.n
               self.dfs(col_num + 1, queen_list + [queen_row[:i] + 'Q' + queen_row[i + 1:]], res)
    
    def queen_judge(self, col, row):
        for k in xrange(col):
            if self.board[k] == row or abs(col - k) == abs(row - self.board[k]):
               return False
        return True

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print matrix[i]

if __name__ == '__main__':
   s = Solution()
   queens = s.solveNQueens(4)
   for queen in queens:
       s.print_matrix(queen)
       print '#################'




