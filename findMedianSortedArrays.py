class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
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
        
s = Solution()
s.findMedianSortedArrays(A, B)
s.findMedianSortedArrays(C, D)