class Solution:
    # @param prices, a list of integer
    # @return an integer
    # Chris:TODO::rewrite the algo by yourslef again.
    def maxProfit(self, prices):
        length = len(prices)
        if length == 0:
           return 0

        minDP = [0 for i in xrange(length)]
        maxDP = [0 for i in xrange(length)]

        minV = prices[0]; maxV = prices[length - 1]
        for i in xrange(1, length):
            minV     = min(minV, prices[i])
            maxV     = max(maxV, prices[length - 1 - i])
            minDP[i] = max(minDP[i - 1], prices[i] - minV)
            maxDP[length - 1 - i] = max(maxDP[length - i], maxV - prices[length - 1 - i])
        
        # for i in xrange(length - 2, -1, -1):
        #     maxV     = max(maxV, prices[i])
        #     maxDP[i] = max(maxDP[i + 1], maxV - prices[i])

        return max([maxDP[i] + minDP[i] for i in xrange(length)])





        