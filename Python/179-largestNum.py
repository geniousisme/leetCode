class Solution:
    # @param {integer[]} nums
    # @return {string}
    # Chris:TODO:: worship the following algo and learn it forever!
    # cmp: please read this article: https://docs.python.org/2/library/functions.html#sorted
    def largestNumber(self, nums):
        new_nums = sorted([str(num) for num in nums], cmp=self.compare)
        num_str  = ''.join(new_nums).lstrip('0')
        return num_str or '0'

    def compare(self, a, b):
        return [1, -1][a + b > b + a] # should put 1 first, but it can reverse the string with the order we want
    

    # def largestNumber(self, nums):
    #     if not sum(nums): return '0'
    #     length = len(nums)
    #     max_digits = max([self.digits(n) for n in nums])
    #     num_tuples = [self.makeup(n, max_digits) for n in nums]
    #     num_tuples.sort()
    #     return ''.join([num_tuples[i][1] for i in xrange(length - 1, -1, -1)])

    # def makeup(self, num, max_digits):
    #     curr_digits = self.digits(num)
    #     diff = max_digits - curr_digits
    #     num_tmp = num * 10 ** diff
    #     unit = num % 10
    #     for i in xrange(diff - 1, -1, -1):
    #         num_tmp += unit * 10 ** i
    #     return (num_tmp, str(num))

    # def digits(self, num):
    #     if num > 0:
    #         digits = int(math.log10(num))+1
    #     elif num == 0:
    #         digits = 1
    #     return digits

if __name__ == '__main__':
   s = Solution()
   print s.largestNumber([3, 30, 34, 5, 9])
