from math import factorial

class Solution:
    # @param {integer} rowIndex
    # @return {integer[]}
    def getRow(self, rowIndex):
        res = []
        f = factorial
        n = rowIndex
        for k in xrange(rowIndex + 1):
            res.append(f(n) / f(k) / f(n - k))
        return res
        
if __name__ == '__main__':
   s = Solution()
   for i in xrange(10):
       print s.getRow(i)



        