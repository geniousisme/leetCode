class Solution:
    # @param {integer[][]} matrix
    # @return {void} Do not return anything, modify matrix in-place instead.
    def setZeroes(self, matrix):
        row_num = len(matrix)
        col_num = len(matrix[0])
        row_idx_list = [False] * row_num 
        col_idx_list = [False] * col_num
        for i in xrange(row_num):
            for j in xrange(col_num):
                if not matrix[i][j]:
                   row_idx_list[i] = True
                   col_idx_list[j] = True
        for i in xrange(row_num):
            if row_idx_list[i]:
               matrix[i] = [0] * col_num
        for j in xrange(col_num):
            if col_idx_list[j]:
               for i in xrange(row_num):
                   matrix[i][j] = 0

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print ' '.join([ str(n) for n in matrix[i]])


if __name__ == '__main__':
   s = Solution()
   matrix = [[3, 4, 5, 9], [8, 0, 0, 1], [1, 7, 1, 9]]
   s.print_matrix(matrix)
   s.setZeroes(matrix)
   s.print_matrix(matrix)

        