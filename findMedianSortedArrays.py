class Solution:
    # @return a float
    # compare the num in two sorted array by order, and store them into 
    # a list, then the median would be the last element(or last two, depends on the length sum) in the arrays
    def juniorFMSA(self, A, B): #complexity = O(m+n)
        medianPos   = len(A + B) / 2
        idxA = idxB = 0
        mergedList = [] 
        while len(mergedList) < medianPos + 1:
              if idxA == len(A):
                mergedList.append(B[idxB])
                idxB += 1
              elif idxB == len(B):
                mergedList.append(A[idxA])
                idxA += 1
              else:
                if A[idxA] >= B[idxB]:  
                  mergedList.append(B[idxB])
                  idxB += 1
                else:
                  mergedList.append(A[idxA])
                  idxA += 1     
        return float(mergedList[-1]) if len(A + B) % 2 == 1 else float(sum(mergedList[-2:])) / 2        
    
    # follow the intruction of this website:
    # http://www.cnblogs.com/zuoyuan/p/3759682.html
    # the time cost is around 130 ~ 140 ms for leetCode test
    def getKth(self, A, B, k):
        if len(A) > len(B):
           return self.getKth(B, A, k)
        if len(A) == 0:
           return B[k - 1]
        if k == 1:
           return min(A[0], B[0])
        pa = min(k/2, len(A))
        pb = k - pa
        if A[pa - 1] < B[pb - 1]:
           return self.getKth(A[pa:], B, pb)
        else:
           return self.getKth(A, B[pb:], pa)
    
    def findMedianSortedArrays(self, A, B): #complexity = O(log(m+n))
        if len(A + B) % 2 == 1:
           return self.getKth(A, B, len(A + B) / 2 + 1)
        else:
           return (self.getKth(A, B, len(A + B) / 2 + 1) + self.getKth(A, B, len(A + B) / 2)) * 0.5 # for return float, multiply 0.5

########################### End of the Code ###########################
s = Solution()
s.findMedianSortedArrays(A, B)
s.findMedianSortedArrays(C, D)