# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if node is None:
           return node
        return self.dfs(node, {})

    def dfs(self, node, table):
        if table.get(node) is not None:
           return table[node]
        next_node = UndirectedGraphNode(node.label)
        table[node] = next_node
        for neighbor in node.neighbors:
            next_node.neighbors.append(self.dfs(neighbor, table))
        return next_node

        