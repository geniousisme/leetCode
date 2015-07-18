#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    
    def __init__(self):
        self.res    = []
        self.length = 0

    def combinationSum2(self, candidates, target):
        self.length = len(candidates)
        candidates.sort()
        self.DFS(target, candidates, [], 0)
        return self.res

    def DFS(self, diff, candidates, comb, start):
        if not diff and comb not in self.res: # diff == 0
        # if not diff: # diff == 0
           self.res.append(comb)
           # print 'res:', self.res
           return self.res
        else:
           for i in xrange(start, self.length):
               if candidates[i] > diff:
                  # print '===== if ======'
                  # print 'curr', candidates[i]
                  # print '# diff:', diff
                  # print '# comb:', comb
                  # print '===== end ====='
                  return
               else:
                  # print 'diff:', diff
                  # print 'comb', comb
                  self.DFS(diff - candidates[i], candidates, comb + [candidates[i]], i + 1)

if __name__ == '__main__':
   s = Solution()
   candidates = [10,1,2,7,6,1,5] 
   target     = 8
   print s.combinationSum2(candidates, target)
   