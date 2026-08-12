''' Structure of doubly linked list Node
  class Node:
      def __init__(self, x):
          self.data = x
          self.next = None
          self.prev = None
'''
class Solution:
    def displayList(self, head):
        
        if not head:
            return [[] , []]
        
        forward = []
        backward = []
        curr = head
        tail = None
        
        while curr:
            forward.append(curr.data)
            tail = curr  
            curr = curr.next
            
        curr = tail
        
        while curr:
            backward.append(curr.data)
            curr = curr.prev
            
        return [forward, backward]