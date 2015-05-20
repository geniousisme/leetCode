class Solution:
    # @return an integer
    import re
    def atoi(self, str):
        matchObj = re.match(r'[-+]*[0-9]+', str.strip()) # left -,+,and numbers only, clean up the whitespce in front & non-num words in the back
        if matchObj: # the str has int string to convert
             matchObjGroup = matchObj.group() # escape the none-type error since I put the group here
             if self.isValidInt(matchObjGroup): # check if the '-' & '+' sign is in valid format or not, which means only one '+' or '-'
                if int(matchObjGroup) > 2 ** 31 - 1: # check if num is overflow in positive way
                    return 2 ** 31 - 1
                elif int(matchObjGroup) < - 2 ** 31: # check if num is overflow in negative way
                    return - 2 ** 31
                else:
                    return int(matchObjGroup)
             else:
                return 0
        else: # no such format in the str, invalid
            return 0
    
    def isValidInt(self, str):
        if str[0] == '-' or str[0] == '+': # check if first index has - or +
           return not (str[1] == '-' or str[1] == '+') # if the next index still has - or +, it is invalid format
        else:
           return True

###### to do #######
# 1. to write an no regular expression version
# 2. if there are any better way to do this

###### self-test case ########
s = Solution()
assert s.atoi('1') == 1
assert s.atoi('1234567890') == 1234567890
assert s.atoi('     +345  7890++HFUHDUE') == 345
assert s.atoi(' -123%^^&&**') == -123
assert s.atoi('     ') == 0
assert s.atoi('') == 0
assert s.atoi('-') == 0

assert s.atoi('--2') == 0
assert s.atoi('+--2') == 0
assert s.atoi('++2') == 0
assert s.atoi('-#$%^&*()') == 0
assert s.atoi('+#$%^&*()') == 0