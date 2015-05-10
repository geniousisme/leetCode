# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def deleteDuplicates(self, head):
        start = ListNode(0); start.next = head; tmp = head
        prev  = None; prev_prev = None
        while head:
              if prev != start.next.val
                 prev = start.next.val
                 start.next = start.next.next
              else: # prev == start.next.val



        