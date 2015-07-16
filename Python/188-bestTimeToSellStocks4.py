class Solution:
    # @param {integer} k
    # @param {integer[]} prices
    # @return {integer}
    # Chris::not really understand abt this problem, need to read more or discuss with others
    def maxProfit(self, k, prices):
        length = len(prices)
        if length == 0:
            return 0
        if 2 * k >= length:
           return self.greedyProfit(length, prices)
        dp    = [None for i in xrange(2 * k + 1)]
        dp[0] = 0
        for i in xrange(length):
            for j in xrange(1, min(2 * k, i + 1) + 1):
                dp[j] = max(dp[j], dp[j - 1] + prices[i] * [1, -1][j % 2])
        return dp[2 * k]

    def greedyProfit(self, length, prices):
        sum = 0
        for i in xrange(1, length):
            if prices[i] > prices[i - 1]:
               sum += prices[i] - prices[i - 1]
        return sum