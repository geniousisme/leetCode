# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @return {boolean}
    def isPalindrome(self, head):          
        fast = slow = head
        half_list = []
        idx = 0
        while fast and fast.next:
              half_list.append(slow.val)
              idx += 1
              slow = slow.next
              fast = fast.next.next
        if fast:
           half_list.append(slow.val)
           idx += 1
        while slow and idx:
              if half_list[idx - 1] != slow.val:
                 return False
              slow = slow.next
              idx  -= 1
        return True 

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
   test = ListNode('a')
   test.next = ListNode('b')
   # test.next.next = ListNode('a')
   # test.next.next.next = ListNode('a')
   # test.next.next.next.next = ListNode('5')

   print s.isPalindrome(test)

        