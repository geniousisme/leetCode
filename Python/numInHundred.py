class Solution:
    def __init__(self):
        self.hundred_dict = {}
        for i in xrange(1, 101):
            self.hundred_dict[i] = 0
    
    def numInHundred(self, num):
        for n in num:
            self.hundred_dict[n] += 1
        for i in xrange(1, 101):
            if not self.hundred_dict[i]:
               print i

if __name__ == '__main__':
   s = Solution()
   num = [i for i in xrange(1, 101)]
   num.remove(3)
   num.remove(7)
   num.remove(9)
   s.numInHundred(num)


