class Solution:
    # @param {integer} k
    # @param {integer} n
    # @return {integer[][]}
    def combinationSum3(self, k, n):
        if k > 0:
           res = []; comb = []
           self.recCombination(0, k, 0, n, comb, res)
        return res            

    def recCombination(self, curr, k, count, left, comb, res):
        if left == 0 and count == k:
           res.append(comb)
           return
        for i in xrange(curr + 1, 10):
            self.recCombination(i, k, count + 1, left - i, comb + [i], res)

if __name__ == '__main__':
   s = Solution()
   print s.combinationSum3(3, 7)
   print s.combinationSum3(3, 9)




        