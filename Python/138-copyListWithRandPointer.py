# Definition for singly-linked list with a random pointer.
class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None

class Solution:
    # @param head, a RandomRandomListNode
    # @return a RandomRandomListNode
    def copyRandomList(self, head):
        if head is None:
           return None
        
        # copy a node right after the linked list nodes.        
        dummy = head
        while dummy:
              tmp = RandomListNode(dummy.label)
              next = dummy.next
              dummy.next = tmp
              tmp.next = next
              dummy = next

        # copy the random pointer.
        tmp = head
        while tmp:
              if tmp.random:
                 tmp.next.random = tmp.random.next
              tmp = tmp.next.next

        # seperate the duplicated nodes from the linked list.
        newhead = head.next
        nummy   = newhead
        dummy   = head
        while nummy.next:
              dummy.next = nummy.next
              dummy = dummy.next
              nummy.next = dummy.next 
              nummy = nummy.next
        dummy.next = None
        nummy.next = None
                
        # self.print_llst(newhead)

        # while head:
        #       if head == newhead:
        #          print 'reference to original'
        #       else:
        #          print 'deep copy'
        #       head = head.next
        #       newhead = newhead.next
        return newhead
    
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
   test = RandomListNode(1)
   test.next = RandomListNode(2)
   test.next.next = RandomListNode(3)
   test.random = test.next.next
   test.next.next.next = RandomListNode(4)
   test.next.next.next.random = test.next
   # test.next.next.next.next = RandomListNode(2)
   # test.next.next.next.next.next = RandomListNode(5)

   s.print_llst(s.copyRandomList(test))



        