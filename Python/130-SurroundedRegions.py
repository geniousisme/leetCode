class Solution:
    # @param {character[][]} board
    # @return {void} Do not return anything, modify board in-place instead.
    def __init__(self):
        self.width  = 0
        self.length = 0
        self.queue  = []
    
    def solve(self, board):
        if board is None or not board:
           return
        self.width  = len(board)
        self.length = len(board[0])
        for j in xrange(self.length):
            self.bfs(board, 0, j)
            self.bfs(board, self.width - 1, j)
        
        for i in xrange(1, self.width - 1):
            self.bfs(board, i, 0)
            self.bfs(board, i, self.length - 1)
        
        for i in xrange(self.width):
            for j in xrange(self.length):
                if board[i][j] == 'O':
                   board[i][j] = 'X'
                elif board[i][j] == 'Y':
                     board[i][j] = 'O'
        # return board    
    
    def bfs(self, board, x, y):
        if board[x][y] == 'O':
           self.queue.append((x, y))
           self.fillup(board, x, y)

        while self.queue:
              i, j = self.queue.pop(0)
              self.fillup(board, i + 1, j)
              self.fillup(board, i - 1, j)
              self.fillup(board, i, j + 1)
              self.fillup(board, i, j - 1)

    def fillup(self, board, x, y):
        if x < 0 or x >= self.width or y < 0 or y >= self.length or board[x][y] != 'O':
           return
        self.queue.append((x, y))
        board[x][y] = 'Y'
            
#     def print_matrix(self, matrix):
#         for i in xrange(len(matrix)):
#             print ' '.join(matrix[i])

# if __name__ == '__main__':
#    s = Solution()
#    test = [                      \
#             ['X', 'X', 'X', 'X'],\
#             ['X', 'O', 'O', 'X'],\
#             ['X', 'X', 'O', 'X'],\
#             ['X', 'O', 'X', 'X'] \
#           ]
#    s.print_matrix(s.solve(test))


