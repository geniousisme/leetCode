class Solution:
    # @param {string} s1
    # @param {string} s2
    # @return {boolean}
    def isScramble(self, s1, s2):
        # print 's1', s1
        # print 's2', s2
        len1 = len(s1); len2 = len(s2)
        if len1 != len2: 
           return False
        if s1 == s2:
           return True
        # if s1 == s2[::-1]:
        #    return True
        list1 = list(s1); list2 = list(s2)
        list1.sort(); list2.sort()
        if list1 != list2:
           return False
        for i in xrange(1, len1):
            if self.isScramble(s1[:i], s2[:i]) and self.isScramble(s1[i:], s2[i:]):
               return True
            if self.isScramble(s1[:i], s2[len1 - i:]) and self.isScramble(s1[i:], s2[:len1 - i]):
               return True
        return False

if __name__ == '__main__':
   s = Solution()
   print s.isScramble("rgeat", "great")
   print s.isScramble("rgtae", "great")






        