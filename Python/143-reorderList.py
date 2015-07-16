# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {void} Do not return anything, modify head in-place instead.
    def reorderList(self, head):
        # find the middle of the linked list
        if head is None or head.next is None:
           return
        
        fast = slow = head
        while fast.next and fast.next.next:
              slow = slow.next
              fast = fast.next.next
        
        # seperate right and left linked list
        mid       = slow.next
        slow.next = None        
        left      = head
        right     = mid

        # reverse the right part of 
        start = None
        while right:
              next       = right.next
              right.next = start
              start      = right
              right      = next
        right = start
        
        # merge two linked list together
        new_start = new = ListNode(0)
        while left:
              new.next = left
              new = new.next
              left = left.next
              if right:
                 new.next = right
                 new = new.next
                 right = right.next
        head = new_start.next

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
   test.next.next.next.next = ListNode(5)
   test.next.next.next.next.next = ListNode(6)
   test.next.next.next.next.next.next = ListNode(7)
   s.reorderList(test)
   s.print_llst(test)




        