class Solution:
    # @param {string} s
    # @return {integer}
    def lengthOfLongestSubstringTwoDistinct(self, s):
        max_len = len(s)
        left = -1; start = 0
        for right in xrange(1, max_len):
            if s[right] == s[right - 1]:
               continue
            elif s[right] != s[right - 1]:
                 if s[right] != s[left]:
                    left = right - 1
                    start = left + 1
                 else:





        