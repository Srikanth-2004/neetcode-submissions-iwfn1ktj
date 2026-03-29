class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        max_heap = []
        res = []
        
        for i, n in enumerate(nums):
            # push (-value, index) into heap
            heapq.heappush(max_heap, (-n, i))
            
            # remove elements out of window
            while max_heap[0][1] <= i - k:
                heapq.heappop(max_heap)
            
            # record answer when window size >= k
            if i >= k - 1:
                res.append(-max_heap[0][0])
        
        return res