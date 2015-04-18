# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reversellst(self, head):
        current = head; last = None
        while current:
              nxt = current.next # help to make the current move forward 
              current.next = last # link current to last
              last = current # last one is current one, order reversed
              current = nxt # move current to next
              print "current:"
              self.print_llst(current)
              print "last:"
              self.print_llst(last)
        return last
    
    def reverse(self, start, end):
        # print '### reverse ###'
        # print 'start:', start.val
        # print 'end:', end.val
        new_start = ListNode(-1); new_start.next = start
        while new_start.next != end:
              tmp = start.next
              start.next = tmp.next
              tmp.next = new_start.next
              new_start.next = tmp
              print "new_start:"
              self.print_llst(new_start)
              print "start"
              self.print_llst(start)
              # print 'start', start.val
              # print 'new_start', new_start.val
              # print '#########'
        return end, start    
    
    def reverseKGroup(self, head, k):
        if not head: return head
        new_head = ListNode(-1); new_head.next = head; start = new_head
        while start.next:
              end = start
              for i in xrange(k - 1):
                  end = end.next
                  if not end.next: return new_head.next
              # print 'start', start.val
              # print 'end', end.val
              start.next, start = self.reverse(start.next, end.next)
              # print '@start.next:', start.next.val
              # print '@start:', start.val
        return new_head.next

    def print_llst(self, head):
        llst = ''
        while head:
              llst += str(head.val)
              if head.next:
                 llst += '->'
              head = head.next
        print llst

if __name__ == '__main__':
   s = Solution()
   test = ListNode(0)
   test.next = ListNode(1)
   test.next.next = ListNode(2)
   test.next.next.next = ListNode(3)
   test.next.next.next.next = ListNode(4)
   test.next.next.next.next.next = ListNode(5)
   s.print_llst(test)
   # s.print_llst(s.reversellst(test))
   s.print_llst(s.reverseKGroup(test, 2))


        