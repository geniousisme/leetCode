class Solution:
    # @param {integer[]} nums
    # @param {integer} target
    # @return {integer}
    def search(self, nums, target):
        pivot          = self.get_pivot(nums)
        original_pivot = 
        sorted_nums = nums[pivot + 1:] + nums[:pivot + 1]
        sorted_idx  = self.binarySearch(sorted_nums, 0, len(nums), target)
        print sorted_idx
        if sorted_idx >= pivot:
           return sorted_idx + len(nums[:pivot + 1])
        else:
           return sorted_idx - len(nums[pivot + 1:])

    def get_pivot(self, nums):
        for i in xrange(1, len(nums)):
            if nums[i - 1] > nums[i]:
               return i - 1
        return -1

    # def get_original_idx(self, sorted_idx, pivot):

    
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
   print s.search([7,8,9,0,1,2,3,4], 4)
   print s.search([7,8,9,0,1,2,3,4], 9)


