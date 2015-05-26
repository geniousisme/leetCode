# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param two ListNodes
    # @return the intersected ListNode
    def getIntersectionNode(self, headA, headB):
        if headA is None or headB is None:
           return True
        dummyA = headA
        while dummyA.next:
              dummyA = dummyA.next
        dummyB = headB
        while dummyB.next:
              dummyB = dummyB.next
              
        return False


            
        
if __name__ == '__main__':
   s = Solution()
   testA = ListNode(1)
   testB = None
   # testB = ListNode(3)
   # testA.next = ListNode(2)
   # testB.next = ListNode(4)
   # testA.next.next = testB.next = ListNode(4)
   # testA.next.next.next = testB.next.next = ListNode(5)
   print s.getIntersectionNode(testA, testB)