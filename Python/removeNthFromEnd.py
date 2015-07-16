# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkList(object):
      def __init__(self):
          self.cur_node = None

      def add_node(self, data):
          new_node = ListNode(0)
          new_node.val = data
          new_node.next = self.cur_node
          self.cur_node = new_node

class Solution:
    # @return a ListNode
    def print_llst(self, head):
        llst = ""
        while head != None:
            llst += str(head.val) + ' '
            head = head.next
        print llst

    def get_all_node_idx_n_length(self, head):
        # return dic = {idx: node_address}
        idx_node_dict = {}
        idx = 0
        while head != None:
              idx_node_dict[idx] = head
              idx += 1
              head = head.next
        return idx_node_dict, idx

    def removeNthFromEnd(self, head, n):
        node_idx_dict, length = self.get_all_node_idx_n_length(head)
        llst = LinkList()
        for idx in xrange(length - 1, -1, -1):
            if idx != length - n:
               llst.add_node(node_idx_dict[idx].val)
        return llst.cur_node


if __name__ == '__main__':
   s = Solution()
   test_llst = ListNode(1)
   test_llst.next = ListNode(3)
   test_llst.next.next  = ListNode(10)
   test_llst.next.next.next = ListNode(5)
   # print s.llst_length(test_llst)
   s.print_llst(s.removeNthFromEnd(test_llst, 4))
