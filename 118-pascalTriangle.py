class Solution:
    # @param {integer} numRows
    # @return {integer[][]}
    def generate(self, numRows):
        if numRows == 0:
           return []
        if numRows == 1:
           return [[1]]
        if numRows == 2:
           return [[1], [1, 1]]
        triangle = [[1], [1, 1]]
        for idx in xrange(2, numRows):
            new_layer = [1]
            for i in xrange(1, idx):
                new_layer.append(triangle[idx - 1][i] + triangle[idx - 1][i - 1])
            new_layer.append(1)
            triangle.append(new_layer)
        return triangle

if __name__ == '__main__':
   s = Solution()
   for i in xrange(1, 10):
       print s.generate(i) 
