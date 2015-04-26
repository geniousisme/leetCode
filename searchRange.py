class Solution:
    # @param A, a list of integers
    # @param target, an integer to be searched
    # @return a list of length 2, [index1, index2]
    def searchRange(self, A, target):
        end = len(A)
        forward = backward = self.binarySearch(A, 0, end, target)
        for i in xrange(forward + 1, end):
            if A[i] != target:
               break
            else:
               forward = i
        for i in xrange(backward - 1, -1, -1):
            if A[i] != target:
               break
            else:
               backward = i
        return [backward, forward]

    def binarySearch(self, A, start, end, target):
        if len(A[start:end]) == 1:
            if A[0] == target:
               return start
            else:
               return -1
        mid = (start + end) / 2
        if A[mid] > target:
           return self.binarySearch(A, start, mid, target)
        elif A[mid] < target:
             return self.binarySearch(A, mid, end, target)
        else: # A[mid] == target
             return mid       

if __name__ == '__main__':
   s = Solution()
   A =  [5, 7, 7, 7, 7, 7, 8, 8, 9, 10]
   # for i in xrange(0, 100):
   #     print s.binarySearch(A, 0, len(A), 9)
   print s.searchRange(A, 8)
        
