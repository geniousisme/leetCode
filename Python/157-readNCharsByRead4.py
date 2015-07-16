# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
# def read4(buf):
def read4(buf):
    global file_content
    i = 0
    while i < len(file_content) and i < 4:
        buf[i] = file_content[i]
        i += 1
    
    if len(file_content) > 4:
        file_content = file_content[4:]
    else:
        file_content = ""
    return i

class Solution:
    # @param buf, Destination buffer (a list of characters)
    
    # @return The number of characters read (an integer)
    
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


if __name__ == "__main__":
    global file_content
    buf = ['' for _ in xrange(100)]
    file_content = "a"
    print buf[:Solution().read(buf, 9)]    
    file_content = "abcdefghijklmnop"
    print buf[:Solution().read(buf, 9)]    