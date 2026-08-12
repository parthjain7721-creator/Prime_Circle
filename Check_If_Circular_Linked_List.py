#class Node:
#    def __init__(self, data):
#        self.data = data
#        self.next = None


class Solution:
    def isCircular(self, head):
        
        
        if not head:
            return True
            
        curr = head.next
        
        
        while curr and curr != head:
            curr = curr.next
            
        
        return curr == head