# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Chris::TODO:need to review this again.
class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        curA = headA; curB = headB
        lenA = lenB = 0
        while curA:
            lenA += 1
            curA = curA.next
        while curB:
            lenB += 1
            curB = curB.next
        curA = headA; curB = headB
        if lenA > lenB:
            for i in xrange(lenA - lenB):
                curA = curA.next
        elif lenB > lenA:
            for i in xrange(lenB - lenA):
                curB = curB.next
        while curB != curA:
            curB = curB.next
            curA = curA.next
        return curA

            
        
if __name__ == '__main__':
   s = Solution()
   testA = ListNode(1)
   # testB = None
   testB = ListNode(3)
   testA.next = ListNode(2)
   # testB.next = ListNode(4)
   testA.next.next = testB.next = ListNode(4)
   testA.next.next.next = testB.next.next = ListNode(5)
   print s.getIntersectionNode(testA, testB).val