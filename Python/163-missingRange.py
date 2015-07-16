class Solution:
    # @param {integer[]} nums
    # @param {integer} lower
    # @param {integer} upper
    # @return {string[]}
    def findMissingRanges(self, nums, lower, upper):
        ranges = []
        if nums:
           if nums[0] > lower:
              nums.insert(0, lower - 1)
           if nums[-1] < upper:
              nums.append(upper + 1)
        else:
           nums = [lower - 1, upper + 1] 
        length = len(nums)
        for i in xrange(1, length):
            if nums[i] - nums[i - 1] == 2:
                 ranges.append(str(nums[i - 1] + 1))
            elif nums[i] - nums[i - 1] > 2:                
                 ranges.append('->'.join([str(nums[i - 1] + 1), str(nums[i] - 1)]))
        return ranges

if __name__ == '__main__':
   s = Solution()
   print s.findMissingRanges([0, 1, 3, 50, 75], 0, 99)
   print s.findMissingRanges([1, 4, 75], 0, 99)
   print s.findMissingRanges([7, 9, 10, 23, 45, 78, 102], 1, 190)
   print s.findMissingRanges([-1000000000,-9999,0,1,2,10,100,1000,999999999,1000000000], -1000000000, 1000000000)
   print s.findMissingRanges([], 1, 1)



        