class Solution:
    # @param {integer[]} numbers
    # @param {integer} target
    # @return {integer[]}
    def twoSum(self, numbers, target):
        start = 0; end = len(numbers) - 1
        while start < end:
              if numbers[end] + numbers[start] > target:
                 end -= 1
              elif numbers[end] + numbers[start] < target:
                   start += 1
              else:
                   return [start + 1, end + 1]

if __name__ == '__main__': 
   s = Solution()
   print s.twoSum([2, 7, 9, 11, 12, 15], 27)


