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
    # @param n,   Maximum number of characters to read (an integer)
    # @return     The number of characters read (an integer)
    # Chris:TODO::review it again! just copy from clean code
    
    def __init__(self):
        self.buffer = ['', '', '', '']
        self.offset = self.bufsize = 0
    
    def read(self, buf, n):
        read_bytes = 0
        eof        = False
        while not eof and read_bytes < n:
              if self.bufsize == 0:
                 self.bufsize = read4(self.buffer)
                 eof          = self.bufsize < 4
              bytes = min(n - read_bytes, self.bufsize)
              for i in xrange(bytes):
                  buf[read_bytes + i] = self.buffer[self.offset + i]
              self.offset = (self.offset + bytes) % 4
              self.bufsize -= bytes
              read_bytes += bytes

        return read_bytes

if __name__ == "__main__":
    global file_content
    sol = Solution()
    buf = ['' for _ in xrange(100)]
    file_content = "ab"
    print buf[:sol.read(buf, 1)]
    print buf[:sol.read(buf, 2)]    

        