class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n=len(heights)
        i,j = 0,n-1
        max_area = 0
        while i<j:
            if heights[i]<heights[j]:
                max_area = max(heights[i]*abs(i-j),max_area)
                i+=1
            else:
                max_area = max(heights[j]*abs(i-j),max_area)
                j-=1
        return max_area