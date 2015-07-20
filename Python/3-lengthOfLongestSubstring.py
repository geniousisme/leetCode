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