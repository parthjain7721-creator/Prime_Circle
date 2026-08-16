class Solution:
    def binarySearch(self, arr, k):
        
        key = k
        low = 0         
        high = len(arr) - 1           
        flag = 0

        while(low<=high):
            mid = (low + high) // 2
            if(arr[mid]==key):
                return True
                
            elif(arr[mid]<key):
                low = mid + 1       
            else:
                high = mid-1
        
        return False