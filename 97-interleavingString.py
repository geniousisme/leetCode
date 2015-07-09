class Solution:
    # @param {string} s1
    # @param {string} s2
    # @param {string} s3
    # @return {boolean}
    # both solution are good:
    # http://www.cnblogs.com/zuoyuan/p/3767650.html
    # http://chaoren.is-programmer.com/posts/42770.html
    def isInterleave(self, s1, s2, s3):
        len1 = len(s1); len2 = len(s2); len3 = len(s3)
        if len1 + len2 != len3:
           return False
        dp = [[False for j in xrange(len1 + 1)] for i in xrange(len2 + 1)]
        dp[0][0] = True
        for j in xrange(1, len1 + 1):
            dp[0][j] = dp[0][j - 1] and s1[j - 1] == s3[j - 1]
        for i in xrange(1, len2 + 1):
            dp[i][0] = dp[i - 1][0] and s2[i - 1] == s3[i - 1]
        # self.print_matrix(dp)
        for i in xrange(1, len2 + 1):
            for j in xrange(1, len1 + 1):
        # Chris:TODO::How to figure out this state function ?
                dp[i][j] = (dp[i - 1][j] and s2[i - 1] == s3[i + j - 1]) or (dp[i][j - 1] and s1[j - 1] == s3[i + j - 1])
        # self.print_matrix(dp)        
        return dp[-1][-1]

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print matrix[i]



if __name__ == '__main__':
   s = Solution()
   # print s.isInterleave('aabcc', 'dbbca', 'aadbbcbcac')
   print s.isInterleave('a', 'b', 'a')
   # print s.isInterleave('aabcc', 'dbbca', "aadbbbaccc")


