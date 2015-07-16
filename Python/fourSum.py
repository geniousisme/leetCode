class Solution:
    # @return a list of lists of length 4, [[val1,val2,val3,val4]]    
    def sum_comb(self, num):
        two_sum_dict = {}
        length = len(num)
        for idx in xrange(length - 1):
            flag = 1
            while idx + flag < length:
                  sum = num[idx] + num[idx + flag]
                  if two_sum_dict.get(sum):
                     two_sum_dict[sum].append((idx, idx + flag))
                  else:
                     two_sum_dict[sum] = [(idx, idx + flag)]
                  flag += 1
        return two_sum_dict

    def fourSum(self, num, target):
        four_sum_set = set(); num_len = len(num)
        if num_len < 4: return []
        num.sort()
        sum_comb_dict = self.sum_comb(num)
        for i in xrange(num_len - 1):
            for j in xrange(i + 1, num_len - 2):
                small_target = target - num[i] - num[j]
                if small_target in sum_comb_dict:
                   for comb in sum_comb_dict[small_target]:
                       if comb[0] > j:
                          four_sum_set.add((num[i], num[j], num[comb[0]], num[comb[1]]))
            # flag = 1
            # while i + flag < num_len - 2: # since last two will be covered by the dict, so you can use it 
            #       small_target = target - num[i] - num[i + flag]
            #       if small_target in sum_comb_dict:
            #          for comb in sum_comb_dict[small_target]:
            #              if comb[0] > i + flag: # key step, dont use value to judge , since value can be reapeted, but idx will not
            #                                     # by juding the index, we can ensure the increasing order.
            #                 four_sum_set.add((num[i], num[i + flag], num[comb[0]], num[comb[1]]))
            #       flag += 1 
        return [list(s) for s in four_sum_set]


if __name__ == '__main__':
   s = Solution()
   num = [1, 0, -1, 0, -2, 2]
   target = 0
   print s.fourSum(num, target)
        
        
