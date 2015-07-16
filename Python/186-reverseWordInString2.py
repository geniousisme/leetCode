class Solution:
    # @param s, a list of 1 length strings, e.g., s = ['h','e','l','l','o']
    # @return nothing
    def reverseWords(self, s):
        length = len(s)
        if length == 0:
           return
        end = length
        for i in xrange(length - 1, -1, -1):
            if s[i] == ' ':
               s.extend(s[i + 1:end])
               s.append(' ')
               end = i
        s.extend(s[:end])
        del s[:length]

 
if __name__ == '__main__':
   s = Solution()
   test = ['h','e','l','l','o', ' ', 'I', ' ', 'a', 'm', ' ', 'C', 'h', 'r', 'i', 's']
   s.reverseWords(test)
   print test
   test = ['h','e','l','l','o']
   s.reverseWords(test)
   print test
   test = [""]
   s.reverseWords(test)
   print test





        