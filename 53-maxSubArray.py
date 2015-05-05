class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        length    = len(nums)
        max_table = [0] * (length + 1)
        for i in xrange(1, length + 1):
            max_table[i] = max(max_table[i - 1], max_table[i - 1] + nums[i - 1], nums[i - 1])
        return max_table[-1]

if __name__ == '__main__':
   s = Solution()
   nums = [-1, 0, -2, 3, 1, 2, -2, 3]
   print s.maxSubArray(nums)
   nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
   print s.maxSubArray(nums)