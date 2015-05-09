class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def myselfRemoveDuplicates(self, nums): # with ordered list
        i = 0; prev = None; last = len(nums) - 1; repeat_len = 0
        # appeared_times = 0
        while i <= last:
              # print 'prev:', prev
              # print 'i', i
              if prev != nums[i]:
                 prev = nums[i]
                 appeared_times = 0
                 repeat_len += 1
                 i += 1 
              else:
                 appeared_times += 1
                 if appeared_times == 1:
                    i += 1
                    repeat_len += 1
                 if appeared_times > 1:
                    nums.pop(i)
                    last -= 1
              # print 'appeared_times:', appeared_times
        # print 'nums:', nums
        return repeat_len
    
    def removeDuplicates(self, nums):
        length = len(nums)
        repeated_times = 1
        prev = 0
        for i in xrange(1, length):
            if nums[i] == nums[i - 1]:
               repeated_times += 1
               if repeated_times <= 2:
                  prev += 1
                  nums[prev] = nums[i]
            else:
               repeated_times = 1
               prev += 1
               nums[prev] = nums[i]
        print nums
        return prev + 1

        
if __name__ == '__main__':
   s = Solution()
   nums = [1,1,1,1,1,2,2,3,3,3,4,5]
   print s.removeDuplicates(nums)
   # print nums

   nums = [0,0,0,0,0]
   print s.removeDuplicates(nums)
   # print nums

   nums = [0, 1]
   print s.removeDuplicates(nums)
   # print nums

