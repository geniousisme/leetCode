# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param head, a ListNode
    # @param k, an integer
    # @return a ListNode
    def reverse(self, start, end):
        new_start = ListNode(0); new_start.next = start
        while new_start.next != end:
              tmp = start.next
              start.next = tmp.next
              tmp.next = new_start.next
              new_start.next = tmp
        return [end, start]

    def reverseKGroup(self, head, k):
        new_head = ListNode(0); new_head.next = head; start = new_head
        while start.next:
              end = start
              for i in xrange(k - 1):
                  end = end.next
                  if not end.next:
                     return new_head.next
              start.next, start = self.reverse(start.next, end.next)
        return new_head.next

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
   test = ListNode(0)
   test.next = ListNode(1)
   test.next.next = ListNode(2)
   test.next.next.next = ListNode(3)
   test.next.next.next.next = ListNode(4)
   test.next.next.next.next.next = ListNode(5)
   s.print_llst(test)
   s.print_llst(s.reverseKGroup(test, 3))



        