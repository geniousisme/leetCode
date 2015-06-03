class Solution:
    # @param {integer[]} ratings
    # @return {integer}
    def candy(self, ratings):
        if not ratings: return 0
        length = len(ratings)
        candy_nums = [1]
        for i in xrange(1, length):
            if ratings[i] > ratings[i - 1]:
               candy_nums.append(candy_nums[i - 1] + 1)
            else:
               candy_nums.append(1)
        sum = candy_nums[length - 1]
        for i in xrange(length - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
               candy_nums[i] = max(candy_nums[i], candy_nums[i + 1] + 1)
            sum += candy_nums[i]
        return sum

if __name__ == '__main__':
   s = Solution() 
   print s.candy([10, 10, 10, 11, 12, 10])
            


