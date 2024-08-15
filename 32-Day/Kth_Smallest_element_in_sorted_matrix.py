import heapq
class Solution(object):
    def kthSmallest(self, matrix, k):
        heap = []
        head_iters = heapq.merge(heap, *matrix)
        heap = list(head_iters)
        return heap[k-1]
        