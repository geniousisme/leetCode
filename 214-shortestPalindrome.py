class Solution:
    # @param {string} s
    # @return {string}
    # Chris::TODO:need to spend a day to figure out what the hell is KMP!!!
    
    def shortestPalindrome(self, s):
        rev_s = s[::-1]
        print 'rev_s', rev_s
        l = s + '#' + rev_s
        print 'l', l
        p = [0] * len(l)
        for i in range(1, len(l)):
            j = p[i - 1]
            while j > 0 and l[i] != l[j]:
                j = p[j - 1]
            p[i] = j + (l[i] == l[j])
        print 'p', p
        return rev_s[:len(s) - p[-1]] + s

if __name__ == '__main__':
   s = Solution()
   print s.shortestPalindrome("aacecaaa")
   print s.shortestPalindrome("abcd")