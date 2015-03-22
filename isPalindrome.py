class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        x = str(x)
        if len(x) % 2 == 1: # odd length, start from the center
           return self.checkPalindrome(x, len(x) / 2, len(x) / 2)
        else:
           return self.checkPalindrome(x, len(x) / 2 - 1, len(x) / 2)
    
    def checkPalindrome(self, x, left, right):
        while left > -1 and right < len(x):
              if x[left] != x[right]:
                 return False
              left  -= 1
              right += 1
        return True

s = Solution()
assert s.isPalindrome(1221) == True
assert s.isPalindrome(123421) == False