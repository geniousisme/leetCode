class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        length = len(nums) + 1
        summation = (length - 1) * length / 2
        return summation - sum(nums)

if __name__ == '__main__':
   s = Solution()
   print s.missingNumber([0])
   print s.missingNumber([0, 1])
   print s.missingNumber([0, 2])

