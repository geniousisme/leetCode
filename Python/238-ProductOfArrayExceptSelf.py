class Solution:
    # @param {integer[]} nums
    # @return {integer[]}
    def productExceptSelf(self, nums):
        length = len(nums)
        res    = [1] * length
        for i in xrange(1, length):
            res[i] *= nums[i - 1] * res[i - 1]

        right_product = 1
        for i in xrange(length - 1, 0, -1):
            res[i - 1] *= nums[i] * right_product
            right_product *= nums[i]

        return res

if __name__ == '__main__':
   s = Solution()
   print s.productExceptSelf([1,2,3,4])
   print s.productExceptSelf([2,5,6,1])

        