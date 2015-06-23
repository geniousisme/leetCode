# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    
    # Chris::TODO:check with the url, 
    # there is a detailed graph which help you understand so much:
    # http://www.cnblogs.com/zuoyuan/p/3700105.html
    
    def insertionSortList(self, head):
        if head is None:
           return head
        current = head
        dummy = ListNode(-999)
        dummy.next = head
        while current.next:
              if current.next.val < current.val:
                 pre = dummy
                 while pre.next.val < current.next.val:
                       pre = pre.next
                 tmp = current.next
                 current.next = tmp.next
                 tmp.next = pre.next
                 pre.next = tmp
              else: # ascending, continue
                 current = current.next
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
   test.next = ListNode(4)
   test.next.next = ListNode(0)
   test.next.next.next = ListNode(3)
   test.next.next.next.next = ListNode(2)
   test.next.next.next.next.next = ListNode(5)

   s.print_llst(s.insertionSortList(test))

