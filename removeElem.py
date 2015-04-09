class Solution:
    # @param    A       a list of integers
    # @param    elem    an integer, value need to be removed
    # @return an integer
    def removeElement(self, A, elem):
        for a in A:
            if a == elem:
               A.remove(a)
        return len(A)

if __name__ == '__main__':
   s = Solution()
   test = [3, 3]
   print s.removeElement([3, 3], 3)
   print test
   

        