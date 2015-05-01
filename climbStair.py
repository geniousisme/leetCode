class Solution:
    # @param {integer} n
    # @return {integer}
    def climbStairs(self, n):
        dp = [1 for i in xrange(n + 1)]
        # dp.extend([] * (n - 1))
        for i in xrange(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]

if __name__ == '__main__':
   s = Solution()
   print s.climbStairs(10)