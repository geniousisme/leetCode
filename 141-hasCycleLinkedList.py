# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param head, a ListNode
    # @return a boolean
    def hasCycle(self, head):
        if head is None or head.next is None: return False
        slow = fast = head
        while fast and fast.next:
              fast = fast.next.next
              slow = slow.next
              if fast == slow:
                 return True
        return False

    def hasCycle(self, head): # with extra space
        node_dict = {}
        while head:
              try:
                  if node_dict[head]:
                     return True
              except:
                  node_dict[head] = 1
              head = head.next
        return False
        