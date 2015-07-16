class Solution:
    def buildTree(self, preorder, inorder):
        if not preorder or not inorder: 
            return None
        first = preorder.pop(0)
        node = TreeNode(first)
        i = inorder.index(first)
        node.left = self.buildTree(preorder, inorder[0:i])
        node.right = self.buildTree(preorder,inorder[i+1:])
        return node     