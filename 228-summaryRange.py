class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        res = []
        if nums:
           prev = str(nums[0]); post = None
           for i in xrange(1, len(nums)):
               if nums[i] == nums[i - 1] + 1:
                  post = '->' + str(nums[i])
                  continue
               res.append(prev + [post, ''][post is None])
               prev = str(nums[i])
               post = None
           res.append(prev + [post, ''][post is None])
        return res

if __name__ == '__main__':
   s = Solution()
   print s.summaryRanges([]) 
   print s.summaryRanges([0,1,2,4,5,7]) 








        