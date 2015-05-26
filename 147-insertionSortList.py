# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def insertionSortList(self, head):
        newhead = ListNode(-1); start = newhead.next = ListNode(head.val)
        dummy = head.next
        while dummy:
              try:
                  while newhead.next and dummy.val > newhead.next.val:
                        newhead.next = newhead.next.next
                  tmp = newhead.next.next
                  newhead.next.next = ListNode(dummy.val)
                  newhead.next.next.next = tmp
                  newhead = start
              except:
                  newhead.next = ListNode(dummy.val)
              dummy = dummy.next
        return start

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += '->'
              head = head.next
        print llst

        # sorted_lst = [lst[0]]
        # for i in xrange(1, len(lst)):
        #     j = 0
        #     try:
        #         while lst[i] > sorted_lst[j]:
        #               j += 1
        #         sorted_lst.insert(j, lst[i])
        #     except:
        #         sorted_lst.append(lst[i])
        # return sorted_lst

if __name__ == '__main__':
   s = Solution()
   # test = [2, 4, 8, 1, 0, 5, 3, 9, 7]
   test = ListNode(1)
   test.next = ListNode(4)
   test.next.next = ListNode(0)
   test.next.next.next = ListNode(3)
   test.next.next.next.next = ListNode(2)
   test.next.next.next.next.next = ListNode(5)

   s.print_llst(s.insertionSortList(test))

