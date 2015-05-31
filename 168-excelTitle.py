class Solution:
    # @return a string
    def convertToTitle(self, num):
        ans = []
        while num:
            ans.insert(0, chr(65 + (num - 1) % 26))
            num = (num - 1) / 26
        return ''.join(ans)

if __name__ == '__main__':
   s = Solution()
   print s.convertToTitle(1)
   print s.convertToTitle(26)
   print s.convertToTitle(27)
   print s.convertToTitle(31)
   print s.convertToTitle(24568)
