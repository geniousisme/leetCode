# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {ListNode}
    def sortList(self, head):
        if head is None or head.next is None:
           return head
        
        fast = head
        slow = head
        while fast.next and fast.next.next:
              slow = slow.next
              fast = fast.next.next
        
        head1     = slow.next
        slow.next = None
        head2     = head
        
        left    = self.sortList(head2)
        right   = self.sortList(head1) 

        # print 'left'
        # self.print_llst(left)
        # print 'right:'
        # self.print_llst(right)
        return self.merge(left, right)
    
    def merge(self, left, right):
        newhead = ListNode(-1)
        dummy   = newhead 
        while left and right:
              if left.val <= right.val:
                 lnext = left.next
                 left.next = None
                 dummy.next = left
                 left = lnext
              else:
                 rnext = right.next
                 right.next = None
                 dummy.next = right
                 right = rnext
              dummy = dummy.next
        
        if left is None:
           dummy.next = right

        if right is None:
           dummy.next = left

        return newhead.next
    
    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += '->'
              head = head.next
        print llst

# Chris:TODO:: below is 3-times faster code, try to figure out why:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# class Solution:
#     # @param head, a ListNode
#     # @return a ListNode
#     def sortList(self, head):
#         if head == None:
#             return None
#         counter = 0 
#         temp = head
#         while temp != None:
#             temp = temp.next
#             counter += 1
#         return self.sort(head, counter)
        
#     def sort(self,head,size):
#         if size ==1:
#             return head
#         list2 = head
#         for i in range(0,size//2):
#             list2 = list2.next
#         list1 = self.sort(head, size//2)
#         list2 = self.sort(list2,size-size//2)
#         return self.merge(list1, size//2, list2, size-size//2)
        
#     def merge(self,list1, sizeList1, list2, sizeList2):
#         dummy = ListNode(0)
#         list = dummy
#         pointer1 = 0
#         pointer2 = 0
#         while pointer1 < sizeList1 and pointer2 < sizeList2:
#             if list1.val<list2.val:
#                 list.next = list1
#                 list1 = list1.next
#                 pointer1 += 1
#             else:
#                 list.next = list2
#                 list2 = list2.next
#                 pointer2 += 1
#             list = list.next
#         while pointer1 < sizeList1:
#             list.next = list1
#             list1 = list1.next
#             pointer1 += 1
#             list = list.next
#         while pointer2 < sizeList2:
#             list.next = list2
#             list2 = list2.next
#             pointer2 += 1
#             list = list.next
#         list.next = None
#         return dummy.next

if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(4)
   test.next.next = ListNode(3)
   test.next.next.next = ListNode(2)
   test.next.next.next.next = ListNode(0)
   test.next.next.next.next.next = ListNode(5)

   # tmp1 = ListNode(0)
   # tmp1.next = ListNode(4)
   # tmp1.next.next = ListNode(2)

   # tmp2 = ListNode(1)
   # tmp2.next = ListNode(3)
   # tmp2.next.next = ListNode(6)
   # tmp2.next.next.next = ListNode(7)

   # s.print_llst(s.merge(tmp1, tmp2))
   s.print_llst(s.sortList(test))













        