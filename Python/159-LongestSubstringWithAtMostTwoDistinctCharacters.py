class Solution:
    # @param {string} s
    # @return {integer}
    def juinorLengthOfLongestSubstringTwoDistinct(self, s):
        two_word_dict     = {}
        distinct_count    = 0
        max_len = tmp_len = 0
        if s:
           for i in xrange(len(s)):
               if two_word_dict.get(s[i], False):
                  tmp_len += 1
                  # diff_idx = i
               else:
                  distinct_count += 1
                  if distinct_count > 2:
                     two_word_dict = {}
                     two_word_dict[s[i]] = True
                     two_word_dict[s[i - 1]] = True
                     j = i - 1
                     while j > 0 and s[j] == s[j - 1]:
                           j -= 1
                     tmp_len = 1 + i - j
                  else:                     
                     two_word_dict[s[i]] = True
                     tmp_len += 1
               max_len = max(max_len, tmp_len)
        return max_len
    
    # take a reference at this website:
    # http://www.tangjikai.com/algorithms/leetcode-159longest-substring-with-at-most-two-distinct-characters
    def lengthOfLongestSubstringTwoDistinct(self, s):
        j = -1; i = 0; length = len(s); max_len = 0
        for k in xrange(1, length):
            if s[k] == s[k - 1]:
               continue
            else:
               if s[k] != s[j]:
                  max_len = max(max_len, k - i)
                  i = j + 1
               j = k - 1
        return max(length - i, max_len)
               




if __name__ == '__main__':
   s = Solution()
   print s.lengthOfLongestSubstringTwoDistinct('eceba')
   print s.lengthOfLongestSubstringTwoDistinct('eecebaaaaa')
   print s.lengthOfLongestSubstringTwoDistinct('ee')
   print s.lengthOfLongestSubstringTwoDistinct("abaccc")
   print s.lengthOfLongestSubstringTwoDistinct('ccaabbb')




