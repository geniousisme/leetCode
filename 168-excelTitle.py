class Solution:
    # @return a string
    def convertToTitle(self, num):
        ans = ''
        while num:
            ans = chr(65 + (num - 1) % 26) + ans
            num = (num - 1) / 26
        return ans

if __name__ == '__main__':
   s = Solution()
   print s.convertToTitle(1)
   print s.convertToTitle(26)
   print s.convertToTitle(27)
   print s.convertToTitle(31)
   print s.convertToTitle(24568)
