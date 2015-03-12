# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class linkedList:
    def __init__(self):
        self.head = None
    
    def addNode(self, value):
        newNode = ListNode(value)
        newNode.next = self.head
        self.head = newNode
    
    def printList(self):
        node = self.head
        while node:
              print node.val
              node = node.next
    
class Solution:
    # @return a ListNode
    def addTwoNumbers(self, l1, l2):
        lstSum = self.getNumInLst(l1) + self.getNumInLst(l2)
        numStrList = list(str(lstSum))
        finalLst = linkedList()
        for ns in numStrList:
            finalLst.addNode(int(ns))
        return finalLst.head
    
    def getNumInLst(self, node):
        tmpStr = ""
        while node:  
              tmpStr = str(node.val) + tmpStr
              node   = node.next
        return int(tmpStr)
