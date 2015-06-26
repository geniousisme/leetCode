# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    # def reverseList(self, head):
    #     if head is None or head.next is None:
    #        return head
    #     new_node = ListNode(-1); last = None
    #     while head:
    #           new_node = ListNode(head.val) 
    #           new_node.next = last
    #           last = new_node
    #           head = head.next
    #     return new_node

    def reverseList(self, head):
        p = head
        start = None
        while p:
            next = p.next
            p.next = start
            start = p
            p = next
        return start

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

   s.print_llst(s.reverse(test))



              
