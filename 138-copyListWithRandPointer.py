# Definition for singly-linked list with a random pointer.
class RandListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomRandListNode
    # @return a RandomRandListNode
    def copyRandomList(self, head):
        dummy = head
        while dummy:
              tmp = RandListNode(dummy.label)
              next = dummy.next
              dummy.next = tmp
              tmp.next = next
              dummy = next
        
        return head

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.label)
              if head.next:
                 llst += '->'
              head = head.next
        print llst



if __name__ == '__main__':
   s = Solution()
   test = RandListNode(1)
   test.next = RandListNode(4)
   test.next.next = RandListNode(0)
   test.next.next.next = RandListNode(3)
   test.next.next.next.next = RandListNode(2)
   test.next.next.next.next.next = RandListNode(5)

   s.print_llst(s.copyRandomList(test ))



        