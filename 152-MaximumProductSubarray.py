class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxProduct(self, nums):
        curr_min = curr_max = MAX = nums[0]
        for i in xrange(1, len(nums)):
            min_tmp = nums[i] * curr_min
            max_tmp = nums[i] * curr_max
            curr_max = max(min_tmp, max_tmp, nums[i])
            curr_min = min(min_tmp, max_tmp, nums[i])
            MAX = max(MAX, curr_max)
        return MAX

if __name__ == '__main__':
   s = Solution()
   print s.maxProduct([2, 3, -2, 4])
   print s.maxProduct([5, 9, 1, 3, 1, 4])
   print s.maxProduct([1, 2, 3, 4, 5])
   print s.maxProduct([1, -2, -5, -3, 0])
   print s.maxProduct([1, -4, -5, 0, -7, -6])
