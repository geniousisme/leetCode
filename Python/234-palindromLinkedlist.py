# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# class Solution:
#     # @param {ListNode} head
#     # @return {boolean}
#     def isPalindrome(self, head):          
#         fast = slow = head
#         half_list = []
#         idx = 0
#         while fast and fast.next:
#               half_list.append(slow.val)
#               idx += 1
#               slow = slow.next
#               fast = fast.next.next
#         if fast:
#            half_list.append(slow.val)
#            idx += 1
#         while slow and idx:
#               if half_list[idx - 1] != slow.val:
#                  return False
#               slow = slow.next
#               idx  -= 1
#         return True 

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):
        if head is None:
            return True
        #find mid node
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        #reverse second half
        
        
        p, last = slow.next, None
        while p:
            next = p.next
            p.next = last
            last, p = p, next
        
        self.print_llst(last)
        self.print_llst(head)
        #check palindrome
        p1, p2 = last, head
        while p1 and p1.val == p2.val:
            p1, p2 = p1.next, p2.next
        
        return p1 is None

    def print_llst(self, head):
        llst = ""
        while head:
              llst += str(head.val)
              if head.next:
                 llst += '->'
              head = head.next
        print 'llst: ' + llst

if __name__ == '__main__':
   s = Solution()
   test = ListNode(1)
   test.next = ListNode(2)
   test.next.next = ListNode(3)
   test.next.next.next = ListNode(2)
   test.next.next.next.next = ListNode(1)

   print s.isPalindrome(test)

        