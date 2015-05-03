class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def firstMissingPositive(self, nums):
        length = len(nums); i = 0
        while i < length:
            if 1 <= nums[i] <= length and nums[nums[i] - 1] != nums[i]:
               nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            else:
               i += 1
        for i in xrange(length):
            if nums[i] != i + 1:
               return i + 1
        return length + 1
# class Solution:
# # @param A, a list of integers
# # @return an integer
# # @a very subtle solution
# def firstMissingPositive(self, A):
#     n=len(A)
#     for i in range(n):
#         if A[i]<=0: A[i]=n+2
#     for i in range(n):
#         if abs(A[i])<=n:
#             curr=abs(A[i])-1
#             A[curr]=-abs(A[curr])
#     for i in range(n):
#         if A[i]>0: return i+1
#     return n+1
    
if __name__ == '__main__':
   s = Solution()
   # print s.get_max_min([3,4,-1,1])
   print s.firstMissingPositive([1,2,0])
   print s.firstMissingPositive([3,4,-1,1])
   print s.firstMissingPositive([3,0, 5, 10])