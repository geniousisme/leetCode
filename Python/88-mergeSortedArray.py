class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def merge(self, nums1, m, nums2, n):
        if not (nums1 and nums2): 
           nums1.extend(nums2)
           return 
        # if nums1[-1] < nums2[0]:
        #    nums1.extend(nums2)
        #    return
        # elif nums1[0] > nums2[-1]:
        #      for n2 in nums2:
        #          nums1.insert(0, n2)
        tmp = [0 for i in xrange(m + n)]
        i1 = i2 = it = 0
        while i1 < m and i2 < n:
              if nums1[i1] > nums2[i2]:
                 tmp[it] = nums2[i2]
                 i2 += 1
              else: # nums[i1] <= nums2[i2]
                 tmp[it] = nums1[i1]
                 i1 += 1
              it += 1
        # print 'i1', i1
        # print 'i2', i2
        # print 'it', it
        while i2 < n:
              tmp[it] = nums2[i2]
              i2 += 1; it += 1 
        while i1 < m:
              tmp[it] = nums1[i1]
              i1 += 1; it += 1
        for i in xrange(m + n):
            nums1[i] = tmp[i] 
        # print nums1
        
if __name__ == '__main__':
   s = Solution()
   nums1 = [4, 10, 13, 17, 20, 25, 30, 41, 0, 0, 0, 0, 0, 0, 0]
   nums2 = [1, 3, 8, 11, 15, 19, 27]
   s.merge(nums1, 8, nums2, 7)
   s.merge([-1,0,1,1,0,0,0,0,0], 4, [-1,0,2,2,3], 5)