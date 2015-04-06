# import sys
# sys.setrecursionlimit(2**31 - 1) # 10000 is an example, try with different values
# above method cannot support for python on mac, will get segmentation fault

# no matter recursive or iteration, it will cause get out of time limit
# especially the max_int case, need to use some faster way to solve this
# the commented codes are the codes not able to get accepted, but I just think 
# the code is pretty, and also I spent lots of time on it, so I don't want to delete them XDDD

class Solution:
    # @return an integer
    # def divide_iteration(self, dividend, divisor):
    #     quotient = 0
    #     while dividend >= divisor and quotient < 2 ** 31 - 1:
    #           dividend -= divisor
    #           quotient += 1
    #     return quotient

    # def negative_divide_iteration(self, dividend, divisor):
    #     quotient = 0
    #     # print "heyhey"
    #     if dividend > divisor:
    #        while dividend > 0 and quotient > - 2 ** 31:
    #              dividend += divisor
    #              quotient -= 1
    #        return quotient
    #     else:
    #        while dividend < 0 and quotient > - 2 ** 31:
    #              dividend += divisor
    #              quotient -= 1
    #        return quotient
    
    def divide(self, dividend, divisor):
        quotient = divisor_sum = 0; flag = 1 
        if (dividend < 0) ^ (divisor < 0): # XOR dividend < 0, divisor < 0
            flag = -1
        dividend = abs(dividend); divisor = abs(divisor)
        while dividend >= divisor:      # divide two level of this algorithm,
              count = 1                 # first, if dividend is still bigger than                                        # than divisor but smaller than divisor_sum
              divisor_sum = divisor     
              while divisor_sum * 2 <= dividend:
                    divisor_sum += divisor_sum
                    count       += count
              dividend -= divisor_sum
              quotient += count 
        result = quotient * flag
        if result > 2 ** 31 - 1:
           return 2 ** 31 - 1
        if result < -2 ** 31:
           return -2 ** 31
        return result
        
        # def divide_recursion(dividend, divisor, count):
        #     if dividend >= divisor:
        #        return divide_recursion(dividend - divisor, divisor, count + 1)
        #     else:
        #        if count < 2 ** 31 - 1:
        #           return count
        #        else:
        #           return 2 ** 31 - 1
        # int_max = 2 ** 31 - 1
        # if dividend > int_max:
        #    return int_max
        # if dividend < 
        # if (dividend < 0) ^ (divisor < 0):
        #     return self.negative_divide_iteration(dividend, divisor)
        # else:
        #     dividend = abs(dividend); divisor = abs(divisor) 
        #     return self.divide_iteration(dividend, divisor)        

if __name__ == "__main__":
   s = Solution()
   print s.divide(2 ** 32, 1)