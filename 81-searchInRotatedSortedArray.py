class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def mySearch(self, nums, target):
        length         = len(nums)
        pivot          = self.get_pivot(nums)
        if pivot < 0: # there is no pivot
          return self.binarySearch(nums, 0, length, target)
        else:      
          post_res  = self.binarySearch(nums[pivot + 1:], 0, length - pivot - 1, target) # search in previous list 
          prev_res  = self.binarySearch(nums[:pivot + 1], 0, pivot + 1, target) # search in post list 
          return post_res or prev_res
          # print nums[pivot + 1:] + nums[:pivot + 1] 
          # return self.binarySearch(nums[pivot + 1:] + nums[:pivot + 1] , 0, length, target)

    def get_pivot(self, nums):
        for i in xrange(1, len(nums)):
            if nums[i - 1] > nums[i]:
               return i - 1
        return -1
    
    def binarySearch(self, nums, start, end, target):
        if len(nums[start:end]) == 1:
           if nums[0] == target:
              return True
           else:
              return False
        mid = (start + end) / 2
        if target > nums[mid]:
           return self.binarySearch(nums, mid, end, target)
        elif target < nums[mid]:
             return self.binarySearch(nums, start, mid, target)
        else:
             return True

    def search(self, nums, target):
        length = len(nums); left = 0; right = length - 1
        while left <= right:
              mid = (left + right) / 2
              if nums[mid] == target: 
                 return True
              if nums[mid] == nums[left] == nums[right]:
                   left  += 1
                   right -= 1
              elif nums[mid] >= nums[left]:
                   if nums[mid] > target >= nums[left]: right = mid - 1
                   else: left = mid + 1
              else: # nums[mid] <= nums[left]:
                   if nums[mid] <= target < nums[left]: left  = mid + 1
                   else: right = mid - 1
        return False



if __name__ == '__main__':
   s = Solution()
   # nums1 = [4, 5, 5, 6, 7, 0, 0, 1, 1, 2, 3, 3, 4, 4]
   # p = s.get_pivot(nums1)
   # print nums1[:p]
   print s.search([4, 5, 5, 6, 7, 0, 0, 1, 1, 2, 3, 3, 4, 4], 7)
   print s.search([3, 1], 3)   

