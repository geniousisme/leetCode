import heapq
from collections import deque

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer[]}
    def maxSlidingWindowWithMaxFunc(self, nums, k):
        res = []
        if nums:
           for i in xrange(len(nums) - k + 1):
               res.append(max(nums[i:i + k]))
        return res

    def maxSlidingWindowWithHeap(self, nums, k):
        res = []
        if nums:
           for i in xrange(len(nums) - k + 1):
               tmp = nums[i:i + k]
               # print tmp
               heapq.heapify(tmp)
               # print 'after:', tmp
               res.append(tmp[-1])
        return res
    # Chris::TODO:NTR!!
    def maxSlidingWindow(self, nums, k):
        res = []
        dq  = deque() 
        for i in xrange(len(nums)):
            while dq and nums[dq[-1]] <= nums[i]:
                  dq.pop()
            dq.append(i)
            if dq[0] == i - k:
               dq.popleft()
            if i >= k - 1:
               res.append(nums[dq[0]])
            # print 'dq', dq
            # print 'res', res
        return res


if __name__ == '__main__':
   s = Solution()
   print s.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3)
   print s.maxSlidingWindow([1], 1)


