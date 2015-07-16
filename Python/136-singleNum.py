class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def mySingleNumber(self, nums):
        num_dict = {}
        for n in nums:
            try: 
                if num_dict[n]:
                   del num_dict[n]
            except:
                num_dict[n] = 1
        return num_dict.keys()[0]

    def singleNumber(self, nums):
        ans = nums[0]
        for i in xrange(1, len(nums)):
            ans ^= nums[i]
        return ans

if __name__ == '__main__':
   s = Solution()
   test = [1, 1, 2, 3, 2, 4, 5, 6, 7, 7, 6, 4, 5, 3, 8]
   print s.singleNumber(test)