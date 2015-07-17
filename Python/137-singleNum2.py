#!/usr/bin/env python
# -*- coding: utf-8 -*-
class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def mySingleNumber(self, nums):
        num_dict = {}
        for n in nums:
            try: 
                if  num_dict[n] == 1:
                    num_dict[n] += 1
                elif num_dict[n] == 2:
                   del num_dict[n]
            except:
                num_dict[n] = 1
        return num_dict.keys()[0]
    '''
    解题思路：这道题就比较难了。也是考察位操作。网上的位操作解法看了好半天也没有得其精髓。
    由于序列中除了那唯一的一个数之外所有的数都是三个三个出现的。
    如果把这些数都转换成二进制，那么二进制数中1的那些位会连续出现三次，我们可以利用这个思路来解题。
    比如：3331222转换成二进制为：11 11 11 01 10 10 10。在第1位上，1出现了4次。第2位上，1出现了6次。
    那么我们把每一位上为1的个数mod 3剩下的1就是我们所求的数，
    比如这个例子：4 mod 3 = 1; 6 mod 3 = 0。这样剩下的二进制位为：01。那最后所求的数就是1了。
    那怎么实现这个想法呢？使用二进制模拟三进制。
    在连续来3个1后清0。使用两个bit位，bit1和bit2。
    初始状态bit1和bit2都是0，即00，在来了第一个1后，变成了01，
    来了第二个1后变成了10，来了第三个1后，变成了11，然后清0为00，
    即：00->01->10->11，然后将11清为00，这个过程就是我们编程的思路。
    比如如果输入序列为：1 1 1 1 1 1 1，
    则变化过程为：00->01->10->11->00->01->10->11->00->01，
    最后剩下的是1，也就得到了结果。
    如果位数多那么以此类推，比如序列为：3 3 3 2 2 2 1。
    则二进制为：11 11 11 10 10 10 01。则低位为1 1 1 0 0 0 1，
    变化过程为：00->01->10->11->00->00->00->00->01，所以低位剩下1。
    高位为：1 1 1 1 1 1 0，变化过程为：00->01->10->11->00->01->10->11->00->00，所以高位剩下0。
    那么最后剩下的是01，也就是1。如果位数更多，可以以此类推。程序中的one相当于bit1，two相当于bit2。
    '''
    #Chris::TODO:need to read one more time in review, cool stuff.
    #Chris::NTR!!
    #Chris::想像成是三位元的進位會比較好理解
    #one: 只有出現一次的數，出現三次＆一次對 XOR 來說都會復原，所以 one 用 XOR
    #two: 出現第二遍的數，高位元，根據 one 的結果保留原本是 1 的位元
    def singleNumber(self, A):
        one = 0; two = 0; three = 0
        for i in range(len(A)):
            two |= A[i] & one   #two为1时，不管A[i]为什么，two都为1
            # print 'two', bin(two)
            one = A[i] ^ one    #异或操作，都是1就进位
            # print 'one', bin(one)
            three = ~(one & two)#以下三步的意思是：如果one和two都为1时，就清0，反之则保持原来状态。
            # print 'three', bin(three)
            one &= three
            # print '# one:', bin(one)
            two &= three
            # print '# two:', bin(two)
            # print '=================='
        return one

if __name__ == '__main__':
   s = Solution()
   # test = [1, 1, 1, 2, 2, 3, 2, 3, 4, 4, 5, 5, 6, 7, 6, 7, 6, 7, 4, 5, 3, 8]
   test = [1, 1, 1, 2, 2, 2, 3]
   print s.singleNumber(test)