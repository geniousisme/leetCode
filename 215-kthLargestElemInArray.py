import random

class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {integer}
    def findKthLargest(self, nums, k):
        
        pivot = random.choice(nums)
        nums1 = []; nums2 = []
        length = len(nums)
        for i in xrange(length):
            if nums[i] > pivot:
                nums1.append(nums[i])
            elif nums[i] < pivot:
                 nums2.append(nums[i])
        if k <= len(nums1):
           return self.findKthLargest(nums1, k)
        elif k > length - len(nums2):
             return self.findKthLargest(nums2, k - (length - len(nums2)))
        else:
             return pivot

if __name__ == '__main__':
   s = Solution()
   test = [2,4,5,6,1,0,3,10]
   print sorted(test)
   print s.findKthLargest(test, 1)



        