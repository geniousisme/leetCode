# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} m
    # @param {integer} n
    # @return {ListNode}
    def reverse(self, head):
        start = None
        while head:
              next      = head.next 
              # print 'next', next
              head.next = start
              # print 'head.next', head.next
              start     = head
              # print 'start', start
              head      = next
              # print 'head', head
              # self.print_llst(head)
              # self.print_llst(start)
              # print '==================================='
        return start

    def reverseBetween(self, head, m, n):
        dummy = ListNode(0)
        tmp   = dummy
        start = head
        for i in xrange(m - 1):
            tmp.next = start
            tmp      = tmp.next
            start    = start.next
        
        rstart = None
        rend   = start
        next   = None
        
        for i in xrange(m, n + 1):
            next = start.next
            start.next = rstart
            rstart = start
            start = next
        
        tmp.next  = rstart
        rend.next = next

        return dummy.next

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += '->'
              head = head.next
        print llst
if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(2)
   test.next.next = ListNode(3)
   test.next.next.next = ListNode(4)
   test.next.next.next.next = ListNode(5)
   s.print_llst(s.reverseBetween(test, 2, 3))



