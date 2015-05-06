# class Solution:
#     # @param {integer[]} nums
#     # @return {integer}
#     def maxSubArray(self, nums):
#         length    = len(nums)
#         dp = [[0 for i in xrange(length + 1)] for j in xrange(3)]
#         # dp[i][0] = prev 
#         # dp[i][1] = end
#         # dp[i][2] = max_sum
#         dp[2][0] = - 2 ** 31
#         for i in xrange(1, length + 1):
#             # print 'i', i
#             new_sum = sum(nums[dp[0][i - 1]:i + 1])
#             # new_sum = dp[1][i] + nums[i - 1]
#             # print new_sum
#             dp[2][i] = max(dp[2][i - 1], new_sum, nums[i - 1])
#             if dp[2][i] == dp[2][i - 1]:
#                dp[0][i] = dp[0][i - 1]
#                # dp[1][i] = dp[1][i - 1]
#             elif dp[2][i] == new_sum:
#                dp[0][i] = dp[0][i - 1]
#                # dp[1][i] = i - 1
#             else: # dp[2][i] == nums[i - 1]:
#                dp[0][i] = i - 1
#                # dp[1][i] = i - 1
#             # dp[1][i] = new_sum
#         # print dp
#         return dp[-1][-1]

class Solution:
    # @param A, a list of integers
    # @return an integer

    # algorithm: compare with three things,
    def juniorMaxSubArray(self, nums):
        last_sum = 0
        max_sum      = -9999
        for i in xrange(len(nums)):
            last_sum = max(last_sum + nums[i], nums[i]) # compare two things first, 1) last sum, from previous maximum idx to current index, 2) current num: if current is bigger than last_sum + self, choose self
            max_sum      = max(last_sum, max_sum) # compare last_max_sum with last sum
        return max_sum

    def maxSubArray(self, nums): # god logic
        last_sum = 0
        max_sum      = -9999
        for i in xrange(len(nums)):
            if last_sum < 0:
               last_sum = 0
            last_sum += nums[i]
            max_sum      =  max(last_sum, max_sum)
        return max_sum


        

if __name__ == '__main__':
   s = Solution()
   nums = [-1, 0, -2, 3, 1, 2, -2, 3]
   print s.maxSubArray(nums)
   nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
   print s.maxSubArray(nums)