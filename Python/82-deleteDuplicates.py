# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        if head is None or head.next is None: return head
        start = ListNode(-99); start.next = head 
        prev = start
        post = start.next
        while prev.next:
              while post.next and prev.next.val == post.next.val:
                    post = post.next
              if post == prev.next:
                 prev = prev.next
                 post = prev.next
              else:
                 prev.next = post.next
        return start.next
              
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
   test.next.next.next = ListNode(2)
   test.next.next.next.next = ListNode(2)
   test.next.next.next.next.next = ListNode(4)
   test.next.next.next.next.next.next = ListNode(4)
   # s.deleteDuplicates(test)
   s.print_llst(s.deleteDuplicates(test))
   





        