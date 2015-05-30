class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def firstRotate(self, nums, k):
        length = len(nums)
        for i in xrange(length - k % length):
            nums.append(nums.pop(0))

    def rotate(self, nums, k):
        length = len(nums)
        end = length - k % length
        nums.extend(nums[:end])
        del nums[:end]
        

if __name__ == '__main__':
   s = Solution()
   nums = [1, 2, 3, 4, 5, 6]
   s.rotate(nums, 7)
   print nums            