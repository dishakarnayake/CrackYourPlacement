import heapq

class Solution:
    def mincostToHireWorkers(self, quality, wage, k) :
        n = len(quality)
        workers = []

        # Calculate and store the wage-to-quality ratio for each worker
        for i in range(n):
            workers.append((wage[i] / quality[i], quality[i]))
        
        # Sort the workers based on their wage-to-quality ratio in ascending order
        workers.sort()

        max_heap = []
        total_quality = 0
        min_cost = float('inf')
        sum_quality = 0

        for ratio, q in workers:
            # Push the negated quality value onto the max heap
            heapq.heappush(max_heap, -q)
            total_quality += q
            sum_quality += q

            # If the size of the max heap exceeds k, pop the minimum quality
            if len(max_heap) > k:
                sum_quality += heapq.heappop(max_heap)

            # Once we have k workers in the max heap, calculate the total cost and update min_cost
            if len(max_heap) == k:
                min_cost = min(min_cost, sum_quality * ratio)

        return min_cost