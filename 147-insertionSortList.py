# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        newhead = ListNode(-9999); newhead.next = ListNode(head.val)
        new_tmp = newhead
        dummy = head.next
        # self.print_llst(start)
        while dummy:
              print 'dummy', dummy.val
              while new_tmp.next and dummy.val > new_tmp.next.val:
                    new_tmp.next = new_tmp.next.next
              # self.print_llst(start)
              tmp = new_tmp.next
              new_tmp.next = ListNode(dummy.val)
              new_tmp.next.next = tmp
              self.print_llst(newhead)
              new_tmp.next = newhead
              dummy = dummy.next
        return newhead

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
   # test = [2, 4, 8, 1, 0, 5, 3, 9, 7]
   test = ListNode(1)
   test.next = ListNode(4)
   test.next.next = ListNode(0)
   test.next.next.next = ListNode(3)
   test.next.next.next.next = ListNode(2)
   test.next.next.next.next.next = ListNode(5)

   s.print_llst(s.insertionSortList(test))

