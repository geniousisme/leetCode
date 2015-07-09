class Solution:
    # @param {integer[][]} dungeon
    # @return {integer}
    def calculateMinimumHP(self, dungeon):
        length = len(dungeon[0])
        width  = len(dungeon)

        dp = [[0 for j in xrange(length)] for i in xrange(width)]

        dp[-1][-1] = max(1, 1 - dungeon[-1][-1])
        
        for j in xrange(length - 2, -1, -1):
            dp[-1][j] = max(1, dp[-1][j + 1] - dungeon[-1][j])

        for i in xrange(width  - 2, -1, -1):
            dp[i][-1] = max(1, dp[i + 1][-1] - dungeon[i][-1])

        for i in xrange(width - 2, -1, -1):
            for j in xrange(length - 2, -1, -1):
                dp[i][j]  = max(1, min(dp[i + 1][j], dp[i][j + 1]) - dungeon[i][j])
        return dp[0][0]

    def print_matrix(self, matrix):
        for i in xrange(len(matrix)):
            print matrix[i]

if __name__ == '__main__':
   s = Solution()
   dungeon = [[-2, -3, 3],[-5, -10, 1],[10, 30, -5]]
   print s.calculateMinimumHP(dungeon)
   dungeon = [[1],[2]]
   print s.calculateMinimumHP(dungeon)


