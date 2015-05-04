from math import factorial

class Solution:
    # @param {integer} n
    # @param {integer} k
    # @return {string}
    def __init__(self):
        self.num_str_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    def getPermutation(self, n, k):
        result_perm  = []
        nums         = self.num_str_list[:n]
        while nums:
              start, index =  self.factorial_range(n, k)
              result_perm.append(nums[start]) # optimized
              nums = nums[:start] + nums[start + 1:] # optimized
              k =  index
              n -= 1
        return ''.join(result_perm)

    def factorial_range(self, n, k):
        f = factorial(n - 1)
        start = (k - 1) / f
        index = k % f 
        if not index: index = f
        return start, index

if __name__ == '__main__':
   s = Solution()
   # print s.factorial_range(2, 1)
   print s.getPermutation(4, 5)