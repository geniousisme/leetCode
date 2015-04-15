#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
        return dp[len(s)][len(p)]
    



if __name__ == '__main__':
   s = Solution()
   # string = 'aaacddde'
   # pattern = 'a*c*...'
   # print s.split_diff_str(string)
   # print s.split_diff_str(pattern)
   # print s.isMatch(string, pattern)   
   string = 'cccaabbbb'
   pattern = 'c*a*b'
   print s.forward_to_diff_str_idx(4, string)
   # print s.split_diff_str(string)
   # print s.split_diff_str(pattern)
   # print s.isMatch('aab', 'c*a*b')   


        