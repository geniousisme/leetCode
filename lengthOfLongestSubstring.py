class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        startPos = 0
        lastPos  = 1
        longestLen = 1 if len(s) > 0 else 0
        while lastPos < len(s):
              if s[lastPos] not in s[startPos:lastPos]:
                 lastPos += 1
                 if lastPos - startPos > longestLen:
                    longestLen = lastPos - startPos
              else:
                 startPos += s[startPos:lastPos].find(s[lastPos]) + 1
                 lastPos  += 1
        return longestLen
        
    
# s = Solution()
# assert s.lengthOfLongestSubstring("aaabbbbbccccdefd") == 4
# # 4
# assert s.lengthOfLongestSubstring("abcabcdef") == 6
# # 6
# assert s.lengthOfLongestSubstring("uqinntq") == 4
# # 2
# assert s.lengthOfLongestSubstring("abb") == 2
# # 2
# assert s.lengthOfLongestSubstring("abbc") == 2
# # 2
# assert s.lengthOfLongestSubstring("abbcd") == 3
# # 3
# assert s.lengthOfLongestSubstring("abbcdef") == 5
# # 5
# assert s.lengthOfLongestSubstring("abbcdefas") == 7
# # 7
# assert s.lengthOfLongestSubstring("abbcdefasb") == 7
# # 7
# assert s.lengthOfLongestSubstring("abbcdefasbc") == 7
# # 7
# assert s.lengthOfLongestSubstring("abbcdefasbcw") == 8
# # 8
