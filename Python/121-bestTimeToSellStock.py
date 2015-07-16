class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        max_diff = 0
        min_price = float('inf')
        for i in xrange(len(prices)):
            if prices[i] < min_price:
               min_price = prices[i]
            if prices[i] - min_price > max_diff:
               max_diff = prices[i] - min_price
        return max_diff

if __name__ == '__main__':
   s = Solution()
   print s.maxProfit([1, 2, 4])

