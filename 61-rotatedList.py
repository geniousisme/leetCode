# # Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} k
    # @return {ListNode}
    # first version code: wrong approach, the complexity will be O(nk), 
    # and cant handle the k is bigger than length of list case

    # def rotateRight(self, head, k):
    #     start = ListNode(-1); start.next = head; new_end = start
    #     if not k: return head
    #     count = k
    #     while start.next:
    #           # print 'new_end val:', new_end.val
    #           # print 'start.next val', start.next.val
    #           tmp = new_start = start.next
    #           count = k
    #           while count:
    #                 count -= 1
    #                 pivot = tmp
    #                 if tmp is None: return head
    #                 tmp = tmp.next
    #           if tmp is None:
    #              # print new_start.val
    #              # print new_start.next.val
    #              # print pivot.val
    #              # print new_end.val
    #              break
    #           new_end    = new_end.next
    #           start.next = start.next.next
    #     if new_end == start: return head
    #     pivot.next = head
    #     new_end.next = None    
    #     return new_start

    def rotateRight(self, head, k):
        if not k: return head
        if head is None: return head
        start = ListNode(-1); start.next = head; new_end = start
        length = 0
        tmp = start
        while tmp.next:
              length += 1
              tmp = tmp.next
        step = length - (k % length)
        tmp.next = start.next
        # print "step:", step
        new_start = head
        for i in xrange(step):
            new_start = new_start.next
            new_end   = new_end.next
            # print 'new_start:', new_start.val
            # print 'new_end:', new_end.val
        new_end.next = None
        return new_start

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += "->"
              head = head.next
        print llst

if __name__ == '__main__':
  s = Solution()
  test = ListNode(1)
  test.next = ListNode(2)
  # test.next.next = ListNode(3)
  # test.next.next.next = ListNode(4)
  # test.next.next.next.next = ListNode(5)
  s.print_llst(test)
  s.print_llst(s.rotateRight(test, 9))
# s.print_llist(s.rotateRight(test, 5))
