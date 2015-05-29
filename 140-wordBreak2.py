class Solution:
    # @param s, a string
    # @param wordDict, a set<string>
    # @return a string[]
    def __init__(self):
        self.res = []

    def wordBreak(self, s, wordDict):
        if self.wordCheck(s, wordDict):
           self.dfs(s, "", wordDict)
        return self.res
    
    def wordCheck(self, s, wordDict):
        dp = [True]
        for i in xrange(1, len(s) + 1):
            dp.append(False)
            for j in xrange(i):
                if dp[j] and s[j:i] in wordDict:
                   dp[i] = True
        return dp[-1]

    def dfs(self, left_s, wordComb, wordDict):
        if not left_s:
           self.res.append(wordComb[1:])
           return
        for i in xrange(1, len(left_s) + 1):
            if left_s[:i] in wordDict:
               self.dfs(left_s[i:], wordComb + ' ' + left_s[:i], wordDict)

    # def wordBreak(self, s, wordDict):
    #     if s and wordDict:
    #        dp = [True]
    #        self.length = len(s)
    #        self.dfs(s, dp, 0, [], wordDict)
    #     return self.res
        
    # def dfs(self, left_s, dp, len_sum, wordComb, wordDict):
    #     if len_sum == self.length:
    #        self.res.append(wordComb)
    #        return
    #     # if left_s[start:end] in wordDict:
    #     #    wordComb.append(left_s[start:end])
    #     for i in xrange(1, len(left_s) + 1):
    #         dp.append(False)
    #         for j in xrange(i):
    #             if dp[j] and left_s[j:i] in wordDict:
    #                dp[i] = True
    #                # print left_s[j:i]
    #                # wordComb.append(left_s[start:end])
    #                self.dfs(left_s[i:], dp, len_sum + i - j, wordComb + [left_s[j:i]], wordDict)
if __name__ == '__main__':
   s = Solution()
   print s.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"])
   print s.wordBreak("a", ["a"])
   print s.wordCheck("", ['a'])


                


