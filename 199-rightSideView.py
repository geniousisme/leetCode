# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[]}
    def rightSideView(self, root):
        nodes = []
        self.levelTraversal(root, 0, nodes)
        return [node[0] for node in nodes]
        
    def levelTraversal(self, root, level, nodes):
        if root:
           if len(nodes) <= level:
              nodes.append([])
           nodes[level].append(root.val)
           self.levelTraversal(root.right, level + 1, nodes)
           self.levelTraversal(root.left,  level + 1, nodes)
        return

# Chris:TODO::Try to write the iterative version like following.
class Solution:
    # @param root, a tree node
    # @return a list of integers
    def rightSideView(self, root):
        ans = []
        if root is None:
            return ans
        queue = [root]
        while queue:
            size = len(queue)
            for r in range(size):
                top = queue.pop(0)
                if r == 0:
                    ans.append(top.val)
                if top.right:
                    queue.append(top.right)
                if top.left:
                    queue.append(top.left)
        return ans

if __name__ == '__main__':
   s = Solution()
   
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.right = TreeNode(5)
   test.left.left = TreeNode(4)
   # test.right.left = TreeNode(6)
   # test.right.right = TreeNode(7)


   print s.rightSideView(test)
        