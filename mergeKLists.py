# class Solution:
#     # @param a list of ListNode
#     # @return a ListNode
#     def mergeKLists(self, lists):
#         dummy = ListNode(0); tmp = dummy
#         if set(lists) == {None}: return lists
#         lists = self.clean_none_node(lists)
#         while lists:
#               lists    = sorted(lists, key = lambda node: node.val)
#               tmp.next = lists[0]
#               lists[0] = lists[0].next
#               if not lists[0]:  
#                  lists.pop(0)
#               tmp      = tmp.next
#         return dummy.next

#     def clean_none_node(self, lists):
#         def is_not_None(head):
#             return head is not None
#         return [node for node in filter(is_not_None, lists)]

    
#     def print_llst(self, head):
#         llst = ""
#         while head:
#               llst += str(head.val) + ' '
#               head = head.next
#         print llst

class Solution:
    # @param a list of ListNode
    # @return a ListNode
    # use sorted will get TLE, so change to heap
    def mergeKLists(self, lists):
        heap = []
        for node in lists:
            if node: 
                heap.append((node.val, node))
        heapq.heapify(heap)
        head = ListNode(0); curr = head
        while heap:
            pop = heapq.heappop(heap)
            curr.next = ListNode(pop[0])
            curr = curr.next
            if pop[1].next: 
                heapq.heappush(heap, (pop[1].next.val, pop[1].next))
    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val) + ' '
              head = head.next
        print llst


if __name__ == "__main__":
   l1 = ListNode(0)
   l1.next = ListNode(4)
   l1.next.next = ListNode(10)
   l2 = ListNode(1)
   l2.next = ListNode(2)
   l2.next.next = ListNode(15)
   l3 = ListNode(7)
   l3.next = ListNode(8)
   l3.next.next = ListNode(9)

   s = Solution()
   ml = s.mergeKLists([l1, l2, l3])
   s.print_llst(ml)
