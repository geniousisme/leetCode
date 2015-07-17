# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        start_node = ListNode(0); tmp = start_node
        if not l1:
           return l2
        if not l2:
           return l1
        while l1 and l2:
              if l1.val > l2.val:
                  tmp.next = l2
                  l2 = l2.next
                  tmp = tmp.next
              else:
                  tmp.next = l1
                  l1 = l1.next
                  tmp = tmp.next
        if not l1:
           tmp.next = l2
        if not l2:
           tmp.next = l1
        return start_node.next

    def sprint_list(self, head):
        llst = ""
        while head != None:
              llst += str(head.val) + ' '
              head = head.next
        return llst

if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(10)
    l2 = ListNode(3)
    l2.next = ListNode(7)
    l2.next.next = ListNode(30)
    s = Solution()
    ml = s.mergeTwoLists(l1, l2)
    print s.sprint_list(ml)


        