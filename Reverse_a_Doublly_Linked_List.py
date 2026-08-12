""" Structure of Doubly Linked List Node
class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
        self.prev = None
"""

class Solution:
    def reverse(self, head):
        
        if not head:
            return None 
            
        curr = head 
        prev_node = None
        
        while curr : 
            curr.prev , curr.next = curr.next , curr.prev
            prev_node = curr 
            curr = curr.prev
            
        return prev_node
    