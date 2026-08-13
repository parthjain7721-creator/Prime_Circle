''' Structure of linked list Node
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
'''
class Solution:
    def pairwiseSwap(self, head):
        
        if not head or not head.next:
            return head
        
        dummy = Node(0)
        dummy.next = head
        prev = dummy
        
        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next
            
            first.next = second.next
            second.next = first
            prev.next = second
            
            prev = first
            
        return dummy.next        