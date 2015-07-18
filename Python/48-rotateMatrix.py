class Solution:
    # @param matrix, a list of lists of integers
    # @return nothing (void), do not return anything, modify matrix in-place instead.
    def juniorRotate(self, matrix):
        rotated_matrix = []
        length = len(matrix[0])
        for j in xrange(length):
            reversed_column = [matrix[i][j] for i in xrange(length - 1, -1, -1)]
            rotated_matrix.append(reversed_column)
        return rotated_matrix

    def semi_in_place_rotate(self, matrix):
        length = len(matrix[0])
        rotated_matrix = [[0 for i in xrange(length)] for j in xrange(length)]
        ri = 0; rj = length - 1
        for i in xrange(length):
            for j in xrange(length):
                rotated_matrix[i + ri + j][rj] = matrix[i][j]           
            ri -= 1; rj -= 1
        return rotated_matrix

    def inPlaceLousyRotate(self, matrix):
        length = len(matrix[0])
        tmp_matrix = [[0 for i in xrange(length)] for j in xrange(length)]
        for i in xrange(length):
            for j in xrange(length):
                tmp_matrix[i][j] = matrix[i][j]
        ri = 0; rj = length - 1
        for i in xrange(0, length):
            for j in xrange(0, length):
                matrix[i + ri + j][rj] = tmp_matrix[i][j]           
            ri -= 1; rj -= 1
    
    def rotate(self, matrix):
        length = len(matrix[0])
        for i in xrange(length):
            for j in xrange(i + 1, length): 
            # only need to swap from the top half triangle part of the matrix, 
            # or you will swap it twice and make it not useful at all
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        for i in xrange(length):
            matrix[i].reverse()

def print_matrix(matrix):
    for row in matrix:
        print ' '.join([str(r) for r in row])


if __name__ == '__main__':
   s = Solution()
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   s.rotate(matrix)
   print_matrix(matrix)
   # matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
   # print_matrix(s.juniorRotate(matrix))