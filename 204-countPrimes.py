class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        if n < 3:
           return 0
        isPrime = [False, False]
        for i in xrange(2, n):
            isPrime.append(True)
        idx = 2
        while idx * idx < n:
              # print 'idx*idx', idx*idx
              if not isPrime[idx]:
                 idx += 1
                 continue
              jdx = idx * idx
              while jdx < n:
                    isPrime[jdx] = False
                    jdx += idx
              idx += 1
        return sum(isPrime[2:])

if __name__ == '__main__':
   s = Solution()
   print s.countPrimes(3)
   print s.countPrimes(10)
   print s.countPrimes(100)
   print s.countPrimes(1000)




