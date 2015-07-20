class Solution:
    # @param s, a string
    # @return an integer
    def juniorlengthOfLastWord(self, s):
        if s:
           s_list = s.strip().split(' ')
           return len(s_list[-1])
        else:
           return 0

    def lengthOfLastWord(self, s):
        if s:
           s = s.strip()
           last_length = 0
           for i in xrange(len(s) - 1, -1, -1):
               if s[i] == ' ':
                  return last_length
               else:
                  last_length += 1
           return last_length
        else:
           return 0

if __name__ == "__main__":
   s = Solution()
   print s.lengthOfLastWord('a abc')
