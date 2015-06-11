# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        start = ListNode(-1)
        start.next = head
        new = start
        
        while start.next:
              if start.next.val == val:
                 # print 'start.next.val', start.next.val
                 start.next = start.next.next
              else:
                 start = start.next

        return new.next

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
   test.next = ListNode(1)
   test.next.next = ListNode(1)
   test.next.next.next = ListNode(4)
   test.next.next.next.next = ListNode(4)
   test.next.next.next.next.next = ListNode(5)
   s.print_llst(s.removeElements(test, 1))
   s.print_llst(s.removeElements(None, 1))



