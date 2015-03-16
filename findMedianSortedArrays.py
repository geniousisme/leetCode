class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        medianPos    = len(A + B) / 2
        medianPrePos = medianPos - 1 if len(A + B) % 2 == 0 else None
        
