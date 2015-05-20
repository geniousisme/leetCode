# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {ListNode} head
    # @return {TreeNode}
    def sortedListToBST(self, head):
        sorted_list = []; length = 0
        while head:
              sorted_list.append(head.val)
              head = head.next
              length += 1
        return self.buildBST(sorted_list, 0, length - 1)
    
    def buildBST(self, lst, start, end):
        if start > end: return None
        mid = (start + end) / 2
        root = TreeNode(lst[mid])
        root.right = self.buildBST(lst, mid + 1, end)
        root.left  = self.buildBST(lst, start, mid - 1)
        return root

