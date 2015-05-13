# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {integer[][]}
    def __init__(self):
        self.queue = []
        self.lv_order = []
    
    def levelOrder(self, root):
        self.queue.append(root)
        self.BFS(root)
        return self.lv_order

    def BFS(self, node): # BFS
        curr_lv = []
        next_lv = []
        while self.queue:
              node = self.queue.pop(0) # LILO
              if node:
                 curr_lv.append(node.val)
                 next_lv.extend([node.left, node.right])
              if not self.queue:
                 if not curr_lv: return
                 self.lv_order.append(curr_lv)
                 self.queue.extend(next_lv)
                 curr_lv = []
                 next_lv = []
    
    # my original thought is not that good, use too much space
    # personally think the dfs with recursive implementation is better.
    
    def preorder(self, root, level, res): # DFS
        if root:
            if len(res) < level+1: res.append([])
            res[level].append(root.val)
            self.preorder(root.left, level+1, res)
            self.preorder(root.right, level+1, res)
    
    def dfsLevelOrder(self, root):
        res=[]
        self.preorder(root, 0, res)
        return res

if __name__ == '__main__':
   s = Solution()
   test = TreeNode(1)
   test.left = TreeNode(2)
   test.right = TreeNode(3)
   test.left.left = TreeNode(4)
   test.right.right = TreeNode(5)
   print s.levelOrder(test)

