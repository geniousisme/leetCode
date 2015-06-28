class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def longestConsecutive(self, nums):
        if not nums:
           return 0
        num_dict = {}
        length  = len(nums)
        
        for num in nums:
            num_dict[num] = 1
        
        tmp_len = max_len = 1
        for n in sorted(num_dict.keys()):
            if num_dict.get(n + 1):
               tmp_len += 1
               max_len = max(max_len, tmp_len)
            else:
               tmp_len = 1
        return max_len

if __name__ == '__main__':
   s = Solution()
   print s.longestConsecutive([100, 200, 101, 102, 1, 2, 3, 4, 6])
   print s.longestConsecutive([0, 1])
   print s.longestConsecutive([1,2,0,1])
   print s.longestConsecutive([0,3,7,2,5,8,4,6,0,1])