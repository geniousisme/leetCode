class Solution:
    # @param {character[][]} matrix
    # @return {integer}
    def maximalSquare(self, matrix):
        width = len(matrix)
        if width == 0: return 0
        lenth = len(matrix[0])
        max_side = 0
        if width * lenth == 1:
           return [0, 1][matrix[0] != '0']

        for y in xrange(lenth):
            matrix[0][y] = int(matrix[0][y])
        
        for x in xrange(1, width):
            matrix[x][0] = int(matrix[x][0])

        for i in xrange(1, width):
            for j in xrange(1, lenth):
                if matrix[i - 1][j - 1] == '0':
                   matrix[i][j] = 0
                else:
                   matrix[i][j] = min(matrix[i - 1][j], matrix[i][j - 1], matrix[i - 1][j - 1]) + 1
                   if matrix[i][j] > max_side:
                      max_side = matrix[i][j]
        return max_side ** 2

if __name__ == '__main__':
   s = Solution()
   test = [                           \
            ['1', '0', '1', '0', '0'],\
            ['1', '0', '1', '1', '1'],\
            ['1', '1', '1', '1', '1'],\
            ['1', '0', '1', '1', '1'] \
          ]
   print s.maximalSquare(test)
   # print test

   test2 = [['1', '0', '1']]
   print s.maximalSquare(test2)

   test3 = ['1']
   print s.maximalSquare(test3)

#Chris:TODO::follow up the question to see if there is anything wrong with the test case.

# class Solution {
# public:
#     int maximalSquare(vector<vector<char>>& matrix) {
#         int n=matrix.size();
#         if(n==0)return 0;
#         int m=matrix[0].size();
#         int max=0;
#        vector<vector<int>> f(n+1,vector<int>(m+1,0));
#        for(int i=1;i<=n;i++)
#         for(int j=1;j<=m;j++)
#         {
#             if(matrix[i-1][j-1]=='0')f[i][j]=0;
#             else
#             {

#                 f[i][j]=min(min(f[i-1][j],f[i][j-1]),f[i-1][j-1])+1;
#                 if(f[i][j]>max)max=f[i][j];
#             }
#         }
#         return max*max;
#     }
# };
