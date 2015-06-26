class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        length = len(s)
        dictionary = {}
        if length == 1:
           return s == t
        for i in xrange(length):
            replace = dictionary.get(s[i])
            if replace:
               if replace != t[i]:
                  return False
            else:
               if t[i] in dictionary.values():
                  return False
               dictionary[s[i]] = t[i]
        return True

if __name__ == '__main__':
   s = Solution()
   print s.isIsomorphic('egg', 'add')
   print s.isIsomorphic('foo', 'bar')
   print s.isIsomorphic('title', 'paper')
   print s.isIsomorphic('ab', 'aa')





        