class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        if not nums:
           return 0
        return max(self.robLinear(nums[1:]), self.robLinear(nums[2:-1]) + nums[0])   

    def robLinear(self, nums):
        if not nums:
           return 0
        dp = [0, nums[0]]
        for i in xrange(2, len(nums) + 1):
            dp.append(max(dp[i - 1], dp[i - 2] + nums[i - 1]))
        return dp[-1]

if __name__ == '__main__':
   s = Solution()
   print s.rob([1, 2, 3, 4, 5])
   print s.rob([3, 2, 1])
   print s.rob([3, 6])
   print s.rob([])


   # print s.rob([4, 5, 0, 6, 8])
        