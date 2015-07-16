import re

class Solution:
    # @param {string} s
    # @return {boolean}
    def isPalindrome(self, s):
        string = ''.join(re.findall('\w*', s))
        return self.checkPalindrome(string.lower())

    def checkPalindrome(self, s):
        start = 0; end = len(s) - 1
        while start <= end:
              if s[start] != s[end]:
                 return False
              start += 1
              end   -= 1
        return True

if __name__ == '__main__':
   s = Solution()
   print s.checkPalindrome('dcabacd')
   print s.checkPalindrome('dcaba')
   
