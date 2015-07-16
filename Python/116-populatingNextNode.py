# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def __init__(self):
        self.nodes = []
    
    def connect(self, root):
        if root is None or root.left is None:
           return
        root.left.next = root.right
        if root.next:
           root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)

    def juniorConnect(self, root):
        self.dfs(root, 0)
    
    def dfs(self, root, level):
        if root:
            if len(self.nodes) < level + 1:
               self.nodes.append(TreeLinkNode(-1))
            self.nodes[level].next = root
            self.nodes[level] = self.nodes[level].next
            self.dfs(root.left,  level + 1)
            self.dfs(root.right, level + 1)
        return

    def print_link_tree(self, root):
        while root:
              tmp = root
              llst = ""
              while tmp:
                    llst += str(tmp.val)
                    if tmp.next:
                       llst += '->'
                    tmp = tmp.next
              print llst
              root = root.left

if __name__ == '__main__':
   s = Solution()
   test = TreeLinkNode(1)
   test.left = TreeLinkNode(2)
   test.right = TreeLinkNode(3)
   test.left.left = TreeLinkNode(4)
   test.left.right = TreeLinkNode(5)
   # test.right.left = TreeLinkNode(6)
   test.right.right = TreeLinkNode(7)
   s.connect(test)
   s.print_link_tree(test)


