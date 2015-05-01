class Solution:
    # @param {integer} x
    # @return {integer}
    def mySqrt(self, x):
        return self.newtonSqrt(x, 1)

    # this is the newton method for square root
    # here is the intro: http://en.wikipedia.org/wiki/Newton's_method
    def newtonSqrt(self, s, pre_result):
        curr_result = 0.5 * (pre_result + float(s) / pre_result)
        if abs(pre_result - curr_result) < 1: 
        # setting the condition as 1 is for faster code, 
        # if you need the higher precison, you should make it smaller
           return int(curr_result)
        else:
           return self.newtonSqrt(s, curr_result)

if __name__ == '__main__':
   s = Solution()
   print s.mySqrt(100)