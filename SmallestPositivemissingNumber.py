class Solution:
    
    #Function to find the smallest positive number missing from the array.
    def missingNumber(self,arr,n):
        #Your code here
        num_set = set(arr)
        i = 1
        while True:
            if i not in num_set:
                return i
            i += 1