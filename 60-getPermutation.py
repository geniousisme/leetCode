from math import factorial

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def __init__(self):
        self.num_str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        self.res          = []
    def getPermutation(self, n, k):
        nums = self.num_str_list[:n]

    def factorial_range(self, n, k):
        f = factorial(n - 1)
        start = (k - 1) / f + 1
        index = k % f 
        if not index: index = f
        return start, index





        
        
    # def DFS()

if __name__ == '__main__':
   s = Solution()
   print s.factorial_range(5, )