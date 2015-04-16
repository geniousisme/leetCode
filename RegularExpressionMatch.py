#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a boolean
    # def isMatch(self, s, p):
    #     dp_table = [[False for i in xrange(len(s) + 1)] for j in xrange(len(p) + 1)]
    #     dp_table[0][0] = True
    #     for 
    def isMatch(self, s, p):
        dp=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0]=True
        self.printDP(s, p, dp)
        print '######'
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>=2:
                    dp[0][i]=dp[0][i-2]
        self.printDP(s, p, dp)
        print "######"
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                print 'p:', p[j-1] 
                if p[j-1]=='.':
                    print 'dp[',i-1,'][',j-1,']:',dp[i-1][j-1]
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    print 'dp[',i,'][',j-1,']:',dp[i][j-1]
                    print 'dp[',i,'][',j-2,']:',dp[i][j-2]
                    print 'dp[',i-1,'][',j,']:',dp[i-1][j]
                    print 's[',i-1,']:', s[i-1]
                    print 'p[',j-2,']:', p[j-2]
                    dp[i][j]=dp[i][j-1] or dp[i][j-2] or (dp[i-1][j] and (s[i-1]==p[j-2] or p[j-2]=='.'))
                else:
                    print 'dp[',i-1,'][',j-1,']:', dp[i-1][j-1]
                    print 's[',i-1,']:', s[i-1]
                    print 'p[',j-1,']:', p[j-1]
                    dp[i][j]=dp[i-1][j-1] and s[i-1]==p[j-1]
                self.printDP(s, p, dp)

        return dp[len(s)][len(p)]
    
    def printDP(self, s, p, dp):
        for i in range(len(s)+1):
            line_data = ""
            for j in range(len(p)+1):
                if dp[i][j]:
                    line_data += "T "
                else:
                    line_data += "F "
            print line_data


if __name__ == '__main__':
   s = Solution()
   # string = 'aaacddde'
   # pattern = 'a*c*...'
   # print s.split_diff_str(string)
   # print s.split_diff_str(pattern)
   # print s.isMatch(string, pattern)   
<<<<<<< HEAD
   string = 'cab'
   pattern = 'c*a*b'
   print s.isMatch(string, pattern)
=======
   # string = 'cccaabbbb'
   # pattern = 'c*a*b'
   # print s.forward_to_diff_str_idx(4, string)
   # print s.split_diff_str(string)
   # print s.split_diff_str(pattern)
   print s.isMatch('cab', 'c*.b*')   
>>>>>>> 97799db4042b01bc83c0f1733223680a39c595aa

   string = '..*'
   pattern = 'cab'
   print s.isMatch(string, pattern)

        