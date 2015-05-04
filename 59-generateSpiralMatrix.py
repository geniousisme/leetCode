class Solution:
    # @param {integer} n
    # @return {integer[][]}
    def generateMatrix(self, n):
        num = 1; direction    = 0
        # length = n
        matrix       = [[0 for i in xrange(n)] for j in xrange(n)]
        right = down = n - 1
        left  = up   = 0
        
        while num < n ** 2 + 1:
            if direction == 0: # to right
               for i in xrange(left, right + 1):
                   matrix[up][i] = num
                   num += 1
               up += 1
            if direction == 1: # to down 
               for i in xrange(up, down + 1):
                   matrix[i][right] = num
                   num += 1
               right -= 1
            if direction == 2: # to left
               for i in xrange(right, left - 1, -1):
                   matrix[down][i] = num
                   num += 1
               down -= 1
            if direction == 3: # to up
               for i in xrange(down, up - 1, -1):
                   matrix[i][left] = num
                   num += 1
               left += 1
            direction = (direction + 1) % 4
        return matrix

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print ' '.join([str(n) for n in matrix[i]])

if __name__ == '__main__':
   s = Solution()
   s.print_matrix(s.generateMatrix(2))







