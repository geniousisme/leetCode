class Solution:
    # @param {integer[][]} matrix
    # @param {integer} target
    # @return {boolean}
    def __init__(self):
        self.target = 0

    def searchMatrixI(self, matrix, target):
        self.target = target
        length = len(matrix)
        size   = len(matrix[0])
        for i in xrange(length):
            if matrix[i][-1] >= target >= matrix[i][0]:
               if self.binarySearch(matrix[i], 0, size):
                  return True
               else:
                  continue
            else:
               if matrix[i][0] > target:
                  break
        return False

    def binarySearch(self, lst, start, end):
        if end == start + 1:
           return lst[start] == self.target
        mid = (start + end) / 2
        if lst[mid] > self.target:
           return self.binarySearch(lst, start, mid)
        elif lst[mid] < self.target:
             return self.binarySearch(lst, mid, end)
        else:
            return True

    def searchMatrixII(self, matrix, target):
        size = len(matrix[0])
        for i in xrange(len(matrix)):
            for j in xrange(size - 1, -1 , -1):
                if matrix[i][j] < target:
                   break
                elif matrix[i][j] == target:
                     return True
                else:
                     continue
        return False

    def searchMatrix(self, matrix, target):
        size = len(matrix[0])
        j = size - 1
        for i in xrange(len(matrix)):
            while j and matrix[i][j] > target:
                  j -= 1
            if matrix[i][j] == target:
               return True
        return False

if __name__ == '__main__':
   s = Solution()
   test =                   \
   [                        \
      [1,   4,  7, 11, 15], \
      [2,   5,  8, 12, 19], \
      [3,   6,  9, 16, 22], \
      [10, 13, 14, 17, 24], \
      [18, 21, 23, 26, 30]  \
   ]
   print s.searchMatrix(test, 1)
   print s.searchMatrix(test, 5)

   print s.searchMatrix(test, 20)
   print s.searchMatrix(test, 30)







        