class Solution:
    
    #Function to find starting point where the truck can start to get through
    #the complete circle without exhausting its petrol in between.
    def tour(self,lis, n):
        #Code here
        start = 0
        total_petrol = 0
        current_petrol = 0
        
        for i in range(n):
            total_petrol += lis[i][0] - lis[i][1]
            current_petrol += lis[i][0] - lis[i][1]
            
            # If current petrol is negative, reset the start point
            if current_petrol < 0:
                start = i + 1
                current_petrol = 0
        
        if total_petrol >= 0:
            return start
        else:
            return -1