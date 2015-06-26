class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        length = len(nums)
        if length == 0:
           return 0
        dp = [0, nums[0]]
        for i in xrange(2, length + 1):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i - 1]))
        return dp[-1]

if __name__ == '__main__':
   s = Solution()
   print s.rob([2, 1, 1, 2])
   print s.rob([3, 4])
   print s.rob([4, 5, 0, 6, 8])

