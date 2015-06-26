# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):

class Solution:
    # @param buf, Destination buffer (a list of characters)
    # @param n,   Maximum number of characters to read ａ(an integer)
    # @return     The number of characters read (an integer)
    
    # Chris:TODO::WTF, still dont understand the read4 function
    def read(self, buf, n):
        idx = 0
        buf4 = ['', '', '', '']
        while True:
              curr = min(read4(buf4), n - idx)
              for i in xrange(curr):
                  buf[idx] = buf4[i]
                  idx += 1
              if curr != 4 or idx == n:
                 return idx


        