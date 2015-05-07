class Solution:
    # @param {integer[][]} grid
    # @return {integer}
    def minPathSum(self, grid):
        m = len(grid)
        n = len(grid[0])
        for i in xrange(1, n):
            grid[0][i] += grid[0][i - 1] 
        for i in xrange(1, m):
            grid[i][0] += grid[i - 1][0]
        for i in xrange(1, m):
            for j in xrange(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        # s.print_matrix(grid)
        return grid[-1][-1]

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print ' '.join([str(n) for n in matrix[i]])

if __name__ == '__main__':
   s = Solution()
   matrix = [             \
                [1, 3, 5],\
                [1, 2, 2],\
                [4, 3, 1],\
            ]
   print s.minPathSum(matrix)
   matrix = [[1, 2, 3, 4, 5]]
   print s.minPathSum(matrix)
   matrix = [[1]]
   print s.minPathSum(matrix)
   matrix = [[1], [1], [1]]
   print s.minPathSum(matrix)