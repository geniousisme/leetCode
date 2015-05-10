# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        dummy = ListNode(-1); dummy.next = head; tmp = dummy
        while tmp.next:
              if tmp.val == tmp.next.val:
                 curr = tmp
                 curr.next = tmp.next.next
              else:
                 tmp = tmp.next
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
   test = ListNode(0)
   test.next = ListNode(0)
   test.next.next = ListNode(0)
   test.next.next.next = ListNode(0)
   test.next.next.next.next = ListNode(0)
   # test.next.next.next.next.next = ListNode(1)
   # test.next.next.next.next.next.next = ListNode(1)
   s.print_llst(test)
   s.print_llst(s.deleteDuplicates(test))
   


                
        