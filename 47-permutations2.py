class Solution:
    # @param num, a list of integer
    # @return a list of lists of integers
    def permuteUnique(self, num):
        num.sort()
        res = []
        visited = [False for itr in xrange(len(num))]
        self.permuteUnique_rec(num, 0, visited, [], res)
        return res
 
    def permuteUnique_rec(self, num, level, visited, stk, res):
        if level == len(num):
           res.append(stk)
        else:
           i = 0
           while i < len(num):
                 if not visited[i]:
                    visited[i] = True
                    self.permuteUnique_rec(num, level + 1, visited, stk + [num[i]], res)
                    visited[i] = False
                    while i < len(num) - 1 and num[i] == num[i + 1]:
                          i += 1
                    i += 1

if __name__ == '__main__':
   s = Solution()
   print s.permuteUnique([1,1,2])
        