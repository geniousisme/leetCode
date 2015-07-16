class Solution:
    # @param {integer[][]} obstacleGrid
    # @return {integer}
    def uniquePathsWithObstacles(self, obstacleGrid):
        # print '================================='
        m = len(obstacleGrid) # row number
        n = len(obstacleGrid[0]) # column number
        # print 'original:'
        # self.print_matrix(obstacleGrid)
        # print '---------'
        
        if obstacleGrid[0][0]:
           return 0
        else:
           obstacleGrid[0][0] = 1
        
        walkable_flag = 1
        for i in xrange(1, m): # walk first column, init
            if obstacleGrid[i][0]:
               walkable_flag = 0
            obstacleGrid[i][0] = walkable_flag        
        if n == 1: return obstacleGrid[-1][-1]
        
        walkable_flag = 1
        for j in xrange(1, n): # wlak first row, init
            if obstacleGrid[0][j]:
               walkable_flag = 0
            obstacleGrid[0][j] = walkable_flag
        # self.print_matrix(obstacleGrid)
        if m == 1: return obstacleGrid[-1][-1]
        
        for i in xrange(1, m): # walk through left matrix
            for j in xrange(1, n):
                if obstacleGrid[i][j]:
                   obstacleGrid[i][j] = 0
                else:
                   obstacleGrid[i][j] = obstacleGrid[i - 1][j] + obstacleGrid[i][j - 1]
        # print 'final_matrix:'
        # self.print_matrix(obstacleGrid)
        # print 'result:'
        return obstacleGrid[-1][-1]

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print ' '.join([str(n) for n in matrix[i]])

if __name__ == '__main__':
   s = Solution()
   obstacleGrid = [\
                   [0, 0, 1, 0],\
                   [0, 0, 0, 0],\
                   [0, 0, 0, 0],\
                  ]
   print s.uniquePathsWithObstacles(obstacleGrid)
   obstacleGrid = [[1, 0]]
   print s.uniquePathsWithObstacles(obstacleGrid)
   obstacleGrid = [[0, 0]]
   print s.uniquePathsWithObstacles(obstacleGrid)
   obstacleGrid = [[0, 1, 0]]
   print s.uniquePathsWithObstacles(obstacleGrid)
   obstacleGrid = [[0],[0]]
   print s.uniquePathsWithObstacles(obstacleGrid)
   obstacleGrid = [[0]]
   print s.uniquePathsWithObstacles(obstacleGrid)
   obstacleGrid = [[1]]
   print s.uniquePathsWithObstacles(obstacleGrid)
   