class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def firstRemoveElement(self, A, elem):
        len_A = len(A)
        tail = len_A - 1
        for head in xrange(len_A - 1, -1, -1):
            if A[head] == elem:
               A[head], A[tail] = A[tail], A[head]
               tail -= 1
        return tail + 1
    
    def removeElement(self, A, elem):
        i = 0
        for a in A:
            if a != elem:
               A[i] = a
               i += 1
        return i

if __name__ == "__main__":
   s = Solution()
   A = [1, 2, 3, 4, 4, 5]
   print s.removeElement(A, 2)
   print A

        