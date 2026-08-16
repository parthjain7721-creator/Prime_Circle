class Solution:
    def floorSqrt(self, n): 
        
       if n == 0 or n == 1:
           return n

       i = 1
       while i * i <= n:
           i += 1

       return i - 1