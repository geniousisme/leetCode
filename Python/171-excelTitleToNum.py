class Solution:
    # @param {string} s
    # @return {integer}
    def titleToNumber(self, s):
        ans = 0
        end = len(s) - 1
        for i in xrange(end, -1, -1):
            ans += (26 ** (end - i)) * (ord(s[i]) - 64) 
        return ans

if __name__ == '__main__':
   s = Solution()
   print s.titleToNumber('A')
   print s.titleToNumber('Z')
   print s.titleToNumber('AA')
   print s.titleToNumber('AE')
   print s.titleToNumber('AZ')
   print s.titleToNumber('BA')
   print s.titleToNumber('AJHX')




        