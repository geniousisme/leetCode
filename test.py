class Solution:
    # @param A, a list of integers
    # @return an integer
    def firstMissingPositive(self, A):
        i = 0
        while i < len(A):
            if 1 <= A[i] <= len(A) and A[A[i]-1] != A[i]:
                A[A[i]-1], A[i] = A[i], A[A[i]-1]
            else:
                i += 1
        print A
        i = 0
        while i < len(A):
            if A[i] != i+1:
                return i+1
            i += 1
        return i+1

if __name__ == '__main__':
   s = Solution()
   # print s.get_max_min([3,4,-1,1])
   print s.firstMissingPositive([1,2,0])
   print s.firstMissingPositive([3,4,-1,1])
   print s.firstMissingPositive([3,0, 5, 10])