#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param {string} s
    # @return {integer}
    def numDecodings(self, s):
        if not s or s[0] == '0': return 0
        length = len(s)
        # if length == 1: return 1s
        dp = [1, 1] # 不一定要先把 dp table 建好，這種後加前的部分只要先有前面兩個就行，後面一個一個 append 上去
        # dp.extend([0 ] )
        for i in xrange(2, length + 1):
            sub = s[i - 2:i]
            if 9 < int(sub) < 27:
               if sub[1] != '0':
                  dp.append(dp[i - 1] + dp[i - 2])
               else:
                  dp.append(dp[i - 2])
            elif s[i - 1] != '0': 
               dp.append(dp[i - 1])
            else:
               return 0
        # print dp
        return dp[-1]

if __name__ == '__main__':
   s = Solution()
   print s.numDecodings('12321')
   print s.numDecodings('10')
   print s.numDecodings('0')