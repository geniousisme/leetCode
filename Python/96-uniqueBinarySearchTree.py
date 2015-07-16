class Solution:
    # @param {integer} n
    # @return {integer}
    def numTrees(self, n):
        dp = [1, 1, 2]
        if n >= 3:
           for k in xrange(3, n + 1):
               dp.append(sum([dp[i] * dp[k - i - 1] for i in xrange(k)]))
        return dp[n]

if __name__ == '__main__':
   s = Solution()
   for i in xrange(21):
       print s.numTrees(i)
   