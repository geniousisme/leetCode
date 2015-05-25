class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a boolean
    # Chris:TODO: figure out how to know that they want to use DP
    def wordBreak(self, s, wordDict):
        dp = [True]
        for i in xrange(1, len(s) + 1):
            dp.append(False)
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                   dp[i] = True
        return dp[-1]
        