class Solution:
    # @param {string} word1
    # @param {string} word2
    # @return {integer}
    def minDistance(self, word1, word2):
        word1_len = len(word1) + 1 
        word2_len = len(word2) + 1
        dp = [[0 for j in xrange(word1_len)] for i in xrange(word2_len)]
        for i in xrange(word2_len):
            dp[i][0] = i
        for j in xrange(word1_len):
            dp[0][j] = j
        for i in xrange(1, word2_len):
            for j in xrange(1, word1_len):
                dp[i][j] = min(dp[i][j -1] + 1, dp[i - 1][j] + 1, dp[i - 1][j - 1] + [0, 1][word2[i - 1] != word1[j -1]])
        return dp[-1][-1]

if __name__ == '__main__':
   s = Solution()
   print s.minDistance('e', 'g')
   print s.minDistance('egg', 'dog')
   print s.minDistance('a', 'ab')






