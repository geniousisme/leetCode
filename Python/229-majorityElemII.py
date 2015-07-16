class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def majorityElement(self, nums):
        elem_dict = {}
        length    = len(nums)
        res       = []
        for i in xrange(length):
            elem_dict[nums[i]] = elem_dict.get(nums[i], 0) + 1
            if elem_dict[nums[i]] > length / 3:
               res.append(nums[i])
               elem_dict[nums[i]] = -length
        return res

if __name__ == '__main__':
   s = Solution()
   print s.majorityElement([1,1,1,1,1,1,1,2,4])
   print s.majorityElement([1,1,1,1,1,1])




        