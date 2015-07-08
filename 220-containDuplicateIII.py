class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @param {integer} t
    # @return {boolean}
    import collections
    # Chri:TODO:: read this website again: http://bookshadow.com/weblog/2015/06/03/leetcode-contains-duplicate-iii/
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        if k < 1 or t < 0:
           return False
        num_dict = collections.OrderedDict()
        for j in xrange(len(nums)):
            key = nums[j] / t
            for i in [key - 1, key, key + 1]:
                if i in num_dict and abs(num_dict[i] - nums[j]) <= t:
                   return True
            num_dict[key] = nums[j]
            if x >= k:
               num_dict.popitem(last=False)
        return False