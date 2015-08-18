class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def singleNumber(self, nums):
        res_dict = {}
        for i in xrange(len(nums)):
            if res_dict.get(nums[i]):
               del res_dict[nums[i]]
            else:
               res_dict[nums[i]] = 1
        return res_dict.keys()

if __name__ == '__main__':
   s = Solution()
   nums = [1, 2, 1, 3, 2, 5]
   print s.singleNumber(nums)


        