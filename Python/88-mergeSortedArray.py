class Solution:
    # @param {integer[]} nums1
    # @param {integer} m
    # @param {integer[]} nums2
    # @param {integer} n
    # @return {void} Do not return anything, modify nums1 in-place instead.
    def mergeI(self, nums1, m, nums2, n):
        if not (nums1 and nums2): 
           nums1.extend(nums2)
           return 
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
        while i2 < n:
              tmp[it] = nums2[i2]
              i2 += 1; it += 1 
        while i1 < m:
              tmp[it] = nums1[i1]
              i1 += 1; it += 1
        for i in xrange(m + n):
            nums1[i] = tmp[i] 

    def mergeII(self, nums1, m, nums2, n):
        total_len = len(nums1)
        nums1.extend(nums1[:m])
        del nums1[:m]
        # print 'nums1', nums1
        idx1 = n; idx2 = 0; i = 0
        while idx1 < total_len and idx2 < n:
              if nums1[idx1] < nums2[idx2]:
                 nums1[i] = nums1[idx1]
                 idx1    += 1
              else:
                 nums1[i] = nums2[idx2]
                 idx2    += 1
              i += 1 
        while idx2 < n:
              nums1[idx2 - n] = nums2[idx2]
              idx2 += 1

    def merge(self, nums1, m, nums2, n):
        idx1 = m - 1; idx2 = n - 1; total_idx = m + n - 1
        while idx2 > -1 and idx1 > -1:
              if nums1[idx1] > nums2[idx2]:
                 nums1[total_idx] = nums1[idx1]
                 idx1 -= 1
              else:
                 nums1[total_idx] = nums2[idx2]
                 idx2 -= 1
              total_idx -= 1
        while idx2 > -1:
              nums1[total_idx] = nums2[idx2]
              idx2 -= 1

if __name__ == '__main__':
   s = Solution()
   # nums1 = [4, 10, 13, 17, 20, 25, 30, 41, 0, 0, 0, 0, 0, 0, 0]
   # nums2 = [1, 3, 8, 11, 15, 19, 27]
   # s.merge(nums1, 8, nums2, 7)
   # s.merge([-1,0,1,1,0,0,0,0,0], 4, [-1,0,2,2,3], 5)
   nums1 = [9,10,11,12,13]
   nums2 = [4,5,6,7]
   s.merge(nums1, 5, nums2, 4)
   print nums1