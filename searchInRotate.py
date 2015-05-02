class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        length         = len(nums)
        pivot          = self.get_pivot(nums)
        if pivot < 0: # there is no pivot
          return self.binarySearch(nums, 0, length, target)
        else:      
          post_idx  = self.binarySearch(nums[pivot + 1:], 0, length - pivot - 1, target)
          prev_idx  = self.binarySearch(nums[:pivot + 1], 0, pivot + 1, target)
          if prev_idx > -1:
             return prev_idx
          elif post_idx > -1:
             return post_idx + pivot + 1
          else:
             return -1

    def get_pivot(self, nums):
        for i in xrange(1, len(nums)):
            if nums[i - 1] > nums[i]:
               return i - 1
        return -1
    
    def binarySearch(self, nums, start, end, target):
        if len(nums[start:end]) == 1:
           if nums[0] == target:
              return start
           else:
              return -1
        mid = (start + end) / 2
        if target > nums[mid]:
           return self.binarySearch(nums, mid, end, target)
        elif target < nums[mid]:
             return self.binarySearch(nums, start, mid, target)
        else:
             return mid

if __name__ == '__main__':
   s = Solution()
   print s.search([4, 5, 6, 0, 1, 2, 3], 1)
   print s.search([3, 1], 0)
   

