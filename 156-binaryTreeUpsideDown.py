# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {TreeNode}
    def upsideDownBinaryTree(self, root):
        tree_order = []
        start = root
        if root:
           tree_order.append(root.val)
           while root:
                 if root.right:
                    tree_order.append(root.right.val)
                 if root.left:
                    tree_order.append(root.left.val)
                 root = root.left
           print tree_order
           new = TreeNode(tree_order.pop()); start = new
           while tree_order:
                 new.left = TreeNode(tree_order.pop())
                 new.right = TreeNode(tree_order.pop())
                 new = new.right

        return start
    
# Chris:TODO::write following again, so sleepy.
class Solution:
    # @param root, a tree node
    # @return root of the upside down tree
    def upsideDownBinaryTree(self, root):
        p, parent, parent_right = root, None, None
        
        while p:
            left = p.left
            p.left = parent_right
            parent_right = p.right
            p.right = parent
            parent = p
            p = left
            
        return parent

if __name__ == '__main__':
   s = Solution()
   
   test = TreeNode(1)
   test.left = TreeNode(2)
   # test.right = TreeNode(3)
   # test.left.left = TreeNode(4)
   # test.left.right = TreeNode(5)

   print s.upsideDownBinaryTree(test)



