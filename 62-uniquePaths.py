class Solution:
    # @param {integer} m
    # @param {integer} n
    # @return {integer}
    def uniquePaths(self, m, n):
        dp = [[1 for i in xrange(n)] for j in xrange(m)]
        for i in xrange(1, m):
            for j in xrange(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        return dp[-1][-1]

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print ' '.join([str(n) for n in matrix[i]])

if __name__ == '__main__':
   s = Solution()
   print s.uniquePaths(3, 3)