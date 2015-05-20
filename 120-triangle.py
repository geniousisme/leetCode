class Solution:
    # @param triangle, a list of lists of integers
    # @return an integer
    def minimumTotal(self, triangle):   
        # length = len(triangle)
        # bottom-up
        for i in xrange(len(triangle) - 2, -1, -1):
            for j in xrange(i + 1):
                triangle[i][j] += min(triangle[i + 1][j], triangle[i + 1][j + 1]) 
        # print triangle
        return triangle[0][0]

if __name__ == '__main__':
   s = Solution()
   triangle = [[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]]
   print s.minimumTotal(triangle)