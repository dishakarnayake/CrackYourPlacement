'''
class Job:
    
    # Job class which stores profit and deadline.
    
    def __init__(self,profit=0,deadline=0):
        self.profit = profit
        self.deadline = deadline
        self.id = 0
'''        

class Solution:
    
    #Function to find the maximum profit and the number of jobs done.
    def JobScheduling(self,Jobs,n):
        
        # code here
        # Sort the jobs based on profit in descending order
        Jobs.sort(key=lambda x: x.profit, reverse=True)
        
        # Find the maximum deadline in the jobs list
        max_deadline = max(job.deadline for job in Jobs)
        
        # Create a slots array to keep track of which time slots are free
        # Initialize with -1 indicating that the slot is empty
        slots = [-1] * (max_deadline + 1)
        
        count_jobs = 0
        max_profit = 0
        
        # Iterate over all the jobs
        for job in Jobs:
            # Try to find a free slot from job.deadline to 1 (latest to earliest)
            for j in range(min(max_deadline, job.deadline), 0, -1):
                if slots[j] == -1:
                    # If a free slot is found, schedule the job
                    slots[j] = job.id
                    count_jobs += 1
                    max_profit += job.profit
                    break
        
        return count_jobs, max_profit