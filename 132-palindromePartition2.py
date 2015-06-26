class Solution:
    # @param {string} s
    # @return {integer}
    def minCut(self, s):
        n = len(s)
        D = [n - i for i in xrange(n + 1)]
        P = [[False for i in xrange(n)] for j in xrange(n)]
        for i in xrange(n - 1, -1, -1):
            for j in xrange(i, n):
                if s[i] == s[j] and (j - i < 2 or P[i + 1][j - 1]):
                   P[i][j] = True
                   D[i] = min(D[i], D[j + 1] + 1)
        # print D
        return D[0] - 1

if __name__ == '__main__' :
   s = Solution()
   print s.minCut('abcba')
   print s.minCut('bccbedbbaba')