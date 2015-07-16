class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def myMajorityElement(self, nums):
        freq_dict = {}
        total = len(nums)
        for n in nums:
            freq_dict[n] = freq_dict.get(n, 0) + 1
            if freq_dict[n] >= round(total * 0.5):
               return n
    
    # Chris:TODO::find the bit manipulation solution and study it!
    
    def majorityElement(self, nums):
        candidate = None
        count     = 0
        for n in nums:  
            if count == 0:
               candidate = n
               count     = 1
            elif n == candidate:
                 count += 1
            else:
                 count -= 1
        return candidate

if __name__ == '__main__':
   s = Solution()
   print s.majorityElement([1, 2, 2, 2, 1, 0])
