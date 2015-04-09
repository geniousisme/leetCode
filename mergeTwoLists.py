# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
      def __init__(self):
          self.cur_node = None
      
      def add_new_node(self, val): 
          new_node = ListNode(0)
          new_node.val = val
          new_node.next = self.cur_node
          self.cur_node = new_node 


class Solution:
    # @param two ListNodes
    # @return a ListNode
    def mergeTwoLists(self, l1, l2):
        