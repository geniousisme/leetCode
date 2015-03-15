class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        startPos = 0
        lastPos  = 1
        #i = 0
        #repeated = []
        longestLen = 1 if len(s) > 0 else 0
        while lastPos < len(s):
              #print "No.", i
              #print "startPos:", startPos
              #print "lastPos:", lastPos
              #print "s[", lastPos, "] =", s[lastPos]
              #print "s[", startPos, ":", lastPos, "] =", s[startPos:lastPos] 
              # repeated.append(s[startPos])
              if s[lastPos] not in s[startPos:lastPos]:
                 #print True
              #   repeated.append(s[lastPos])
                 lastPos += 1
                 longestLen = lastPos - startPos
              else:
                 startPos += 1
                 lastPos  += 1
              # if lastPos - startPos > 1 and lastPos < len(s) and s[lastPos - 1] in s[startPos:lastPos]:
                 if lastPos - startPos > 1 and s[lastPos - 1] in s[startPos:lastPos - 1]:
                    startPos += 1
              #i += 1
        return longestLen
      
    # def checkRepeated(self, s):
    #     repeated = []
    #     for i in xrange(0, len(s)):
    #         if s[i] in repeated:
    #            return True
    #         else:
    #            repeated.append(s[i])
    #     return False





        
    
s = Solution()
assert s.lengthOfLongestSubstring("aaabbbbbccccdefd") == 4
# 4
assert s.lengthOfLongestSubstring("abcabcdef") == 6
# 6
assert s.lengthOfLongestSubstring("uqinntq") == 4
# 2
assert s.lengthOfLongestSubstring("abb") == 2
# 2
assert s.lengthOfLongestSubstring("abbc") == 2
# 2
assert s.lengthOfLongestSubstring("abbcd") == 3
# 3
assert s.lengthOfLongestSubstring("abbcdef") == 5
# 5
assert s.lengthOfLongestSubstring("abbcdefas") == 7
# 7
assert s.lengthOfLongestSubstring("abbcdefasb") == 7
# 7
assert s.lengthOfLongestSubstring("abbcdefasbc") == 7
# 7
assert s.lengthOfLongestSubstring("abbcdefasbcw") == 8
# 8
