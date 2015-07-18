import heapq

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindow(self, nums, k):
        res = []
        # if nums:
        #    for i in xrange(len(nums) - k + 1):
        #        res.append(max(nums[i:i + k]))
        # return res
        if nums:
           for i in xrange(len(nums) - k + 1):
               tmp = nums[i:i + k]
               print tmp
               heapq.heapify(tmp)
               print 'after:', tmp
               res.append(tmp[-1])
        return res

if __name__ == '__main__':
   s = Solution()
   print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)

