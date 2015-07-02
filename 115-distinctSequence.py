class Solution:
    # @param {string} s
    # @param {string} t
    # @return {integer}
    def numDistinct(self, s, t):
        slen = len(s); tlen = len(t)
        dp = [[0 for j in xrange(tlen + 1)] for i in xrange(slen + 1)]
        for i in xrange(slen + 1):
            dp[i][0] = 1

        # self.print_matrix(dp)
        
        for i in xrange(1, slen + 1):
            for j in xrange(1, tlen + 1):
                if s[i - 1] == t[j - 1]:
                   dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j] 
                else:
                   dp[i][j] = dp[i - 1][j]

        # self.print_matrix(dp)

        return dp[slen][tlen]
    
    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print matrix[i]

if __name__ == '__main__':
   s = Solution()
   print s.numDistinct("rabbbit", "rabbit")