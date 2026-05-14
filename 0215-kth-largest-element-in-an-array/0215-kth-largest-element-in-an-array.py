import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # We maintain a min-heap of size k
        min_heap = []
        
        for num in nums:
            heapq.heappush(min_heap, num)
            
            # Keep only the k largest elements seen so far
            if len(min_heap) > k:
                heapq.heappop(min_heap)
        
        # The root of the heap is the kth largest element
        return min_heap[0]