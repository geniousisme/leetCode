class Solution:
    # @return a string
    def juniorLongestPalindrome(self, s):
        if len(s) <= 1: return s # for empty stirng and single char case
        longestPalin = ""
        for idx in xrange(len(s)):
            oddTmpPalin  = self.getLongestPalindrome(s, idx, idx)
            evenTmpPalin = self.getLongestPalindrome(s, idx, idx + 1)
            if len(oddTmpPalin)  > len(longestPalin):
               longestPalin = oddTmpPalin
            if len(evenTmpPalin) > len(longestPalin):
               longestPalin = evenTmpPalin
        return longestPalin
            
    def getLongestPalindrome(self, s, left, right):
        while left > -1 and right < len(s) and s[left] == s[right]:
              left  -= 1
              right += 1
        return s[left + 1 : right]
        
    def longestPalindrome(self, s):
        pass
###### to do #######
# write the O(N) version
