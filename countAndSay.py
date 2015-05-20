class Solution:
    # @return a string
    def countAndSay(self, n):
        def countStr(n, string):
            if not n:
               return string
            count = 1; prev  = string[0]; result = ""; str_len = len(string)
            for i in xrange(1, str_len + 1):
                if i == str_len:
                   result = "".join([result, str(count), prev])
                   break
                if prev != string[i]:
                   result = "".join([result, str(count), prev])
                   count = 0
                count += 1
                prev = string[i]
            return countStr(n - 1, result)

        if n >= 1:
           return countStr(n - 1, "1")
        else:
           return ""

if __name__ == '__main__':
   s = Solution()
   print s.countAndSay(0)

        
            





