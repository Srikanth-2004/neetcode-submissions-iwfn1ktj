class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        i,j=0,n-1
        max_area = 0
        while i<j:
            mins = min(heights[i],heights[j])
            area = mins*abs(i-j)
            max_area = max(area,max_area)
            if heights[i]>heights[j]:
                j-=1
            else:
                i+=1
        return max_area