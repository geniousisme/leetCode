#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param candidates, a list of integers
    # @param target, integer
    # @return a list of lists of integers
    # 一個自己在寫的時候也會犯的錯誤，到底何謂 back tracking ? 為什麼這算是 back tracking 呢？這提供了很好的解釋！
    # 您好！这道题目我在用递归的时候，如果将这句代码：self.DFS(candidates, target - candidates[i], i, valuelist + [candidates[i]])
    # 改为：valuelist.append(candidates[i]); self.DFS(candidates, target - candidates[i], i, valuelist) 
    # 就会出现了timeout 的error。不知道原因是什么？在用append的时候消耗的时间会更大吗？谢谢！
    # 不是的。如果使用append的话，valuelist的值就改变了，而dfs是要回溯的，所以不能改变valuelist的值，
    # 但要传递的参数是valuelist+[candidates[i]]，相当于a += 1和a+1的区别，
    # 一个a的值改变了，一个没有改变。

    def __init__(self):
        self.res    = []
        self.length = 0

    def combinationSum(self, candidates, target):
        self.length = len(candidates)
        candidates.sort()
        self.DFS(target, candidates, [], 0)
        return self.res

    def DFS(self, diff, candidates, comb, start):
        if not diff: # diff == 0
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
                  self.DFS(diff - candidates[i], candidates, comb + [candidates[i]], i)

if __name__ == '__main__':
   s = Solution()
   candidates = [3,6,7,2]
   target     = 7
   print s.combinationSum(candidates, target)
   