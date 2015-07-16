class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        profit_sum = 0
        for i in xrange(1, len(prices)):
            diff = prices[i] - prices[i - 1]
            if diff > 0:
               profit_sum += diff
        return profit_sum

if __name__ == '__main__':
   s = Solution()
   print s.maxProfit([5, 0, 1, 2, 3, 4])
