# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        length = 0
        start = head
        last = None
        while start:
              length += 1
              new = ListNode(start.val)
              new.next = last
              last = new
              start = start.next

        new_next  = new
        new_start = head
        count = 0

        while count < length:
              if count % 2 == 0:
                 head_next = head.next
                 head.next = new_next
                 head      = head_next
              else:
                 new_next = new.next
                 new.next = head_next
                 new      = new_next
              count += 1
        head = None
        # head.next = None
        # new = None
        new.next = None
        return new_start




        # return new

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += '->'
              head = head.next
        print 'llst: ' + llst

if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(2)
   test.next.next = ListNode(3)
   test.next.next.next = ListNode(4)
   # test.next.next.next.next = ListNode(5)
   s.print_llst(s.reorderList(test))




        