class Solution:
    # @param {integer} n
    # @return {string[][]}
    # Chris::TODO: write the iterative version tomorrow
    def totalNQueens(self, n):
        self.n = n
        self.board = [-1 for i in xrange(self.n)]
        self.count = 0
        self.dfs(0)
        return self.count
    
    def dfs(self, col_num):
        if col_num == self.n:
           self.count += 1
           return
        for i in xrange(self.n):
            if self.queen_judge(col_num, i):
               self.board[col_num] = i
               self.dfs(col_num + 1)
    
    def queen_judge(self, col, row):
        for k in xrange(col):
            if self.board[k] == row or abs(col - k) == abs(row - self.board[k]):
               return False
        return True

if __name__ == '__main__':
   s = Solution()
   print s.totalNQueens(4)
   # for queen in queens:
   #     s.print_matrix(queen)
   #     print '#################'




