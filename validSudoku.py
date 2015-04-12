class Solution:
    # @param board, a 9x9 2D array
    # @return a boolean
    def __init__(self):
        self.sudoku = {        \
                        '1':0, \
                        '2':0, \
                        '3':0, \
                        '4':0, \
                        '5':0, \
                        '6':0, \
                        '7':0, \
                        '8':0, \
                        '9':0
                      }
        
    def clean_sudoku(self):
        return {       \
                '1':0, \
                '2':0, \
                '3':0, \
                '4':0, \
                '5':0, \
                '6':0, \
                '7':0, \
                '8':0, \
                '9':0
               }
    
    def isValidSudoku(self, board=None):
        # check each block first
        count = 0
        for start in xrange(0, 9, 3):
            for i in xrange(0, 9):
                for j in xrange(start, start + 3):
                    count += 1
                    if board[i][j] != '.':
                       if self.sudoku[board[i][j]] > 0:
                          return False
                       else:
                          self.sudoku[board[i][j]] += 1
                    if count == 9: 
                       count = 0
                       self.sudoku = self.clean_sudoku()
        # check row            
        for i in xrange(0, 9):
            for j in xrange(0, 9):
                if board[i][j] != '.':
                   if self.sudoku[board[i][j]] > 0:
                      return False
                   else:
                      self.sudoku[board[i][j]] += 1
            self.sudoku = self.clean_sudoku()

        for i in xrange(0, 9):
            for j in xrange(0, 9):
                if board[j][i] != '.':
                   if self.sudoku[board[j][i]] > 0:
                      return False
                   else:
                      self.sudoku[board[j][i]] += 1
            self.sudoku = self.clean_sudoku()

        return True


# not bad solution:
# class Solution:
#     # @param board, a 9x9 2D array
#     # @return a boolean
#     def isValidSudoku(self, board):
#         def isValid(x, y, tmp):
#             for i in range(9):
#                 if board[i][y]==tmp:return False
#             for i in range(9):
#                 if board[x][i]==tmp:return False
#             for i in range(3):
#                 for j in range(3):
#                     if board[(x/3)*3+i][(y/3)*3+j]==tmp: return False
#             return True
#         for i in range(9):
#             for j in range(9):
#                 if board[i][j]=='.':continue
#                 tmp=board[i][j]
#                 board[i][j]='D'
#                 if isValid(i,j,tmp)==False: return False
#                 else:
#                     board[i][j]=tmp
#         return True

if __name__ == '__main__':
   s = Solution()
   s.isValidSudoku()

        