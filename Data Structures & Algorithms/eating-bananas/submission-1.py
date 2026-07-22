class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        i,j = 1,max(piles)
        min_val = j
        while i<=j:
            k = (i+j)//2
            total_hours = 0
            for p in range(len(piles)):    
                total_hours += math.ceil(piles[p]/k)
            if total_hours <= h:
                min_val = k
                j = k-1
            else:
                i = k+1
        return min_val