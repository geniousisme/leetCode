class Solution:
    # @return an integer
    def reverse(self, x):
        negativeFlag = -1 if x < 0 else 1 # negative case
        xStr = str(abs(x)) # eliminate the negative case
        x    = ""
        for xs in list(xStr):
            x = xs + x
        return int(x) * negativeFlag if int(x) <= 2 ** 31 else 0
###### to do #######
# if there are any better way to do this

###### self-test case ########
s = Solution()
assert s.reverse(123) == 321
assert s.reverse(-321) == -123
assert s.reverse(-10000000000000) == -1
assert s.reverse(1534236469) == 0
assert s.reverse(-2147483648) == 0

