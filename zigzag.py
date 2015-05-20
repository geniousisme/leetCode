class Solution:
    # @return a string
    def convert(self, s, nRows):
        if s == '' or nRows >= len(s): return s
        zigzag = [s[i] for i in xrange(nRows)]
        diff1 = nRows * 2 - 2;  diff2 = 0
        for i in xrange(nRows):
            idx = i; switch = 1
            while True:
                  if switch % 2 == 1 and diff1 > 0:
                     if idx + diff1 > len(s) - 1:   
                        break
                     else:
                        zigzag[i] += s[idx + diff1]
                        idx       += diff1
                  if switch % 2 == 0 and diff2 > 0:
                     if idx + diff2 > len(s) - 1:   
                        break
                     else:
                        zigzag[i] += s[idx + diff2]
                        idx       += diff2
                  switch += 1
            diff1 -= 2; diff2 += 2
        return "".join(zigzag)

###### self-test case ########
        
