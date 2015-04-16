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




    # def reverseKGroup(self, head, k):


if __name__ == '__main__':
   s = Solution()
   test = ListNode(0)
   test.next = ListNode(1)
   test.next.next = ListNode(2)
   test.next.next.next = ListNode(3)
   test.next.next.next.next = ListNode(4)
   test.next.next.next.next.next = ListNode(5)


        