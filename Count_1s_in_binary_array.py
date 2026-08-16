class Solution:
    def countOnes(self, arr):
        count = 0 
        
        for num in arr : 
            if num == 1:
                count += 1 
                
        return count
