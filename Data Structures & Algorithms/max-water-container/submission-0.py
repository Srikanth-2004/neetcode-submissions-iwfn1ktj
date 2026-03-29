class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l,r = 0,len(heights)-1
        max_area = float('-inf')
        while l<r:
            max_area = max(max_area, min(heights[l],heights[r]) * abs(l-r))
            if heights[l]>heights[r]:
                r-=1
            elif heights[l]<heights[r]:
                l+=1
            elif heights[l]==heights[r]:
                if heights[l+1]>heights[r-1] and (l+1)!=(r-1):
                    l+=1
                elif heights[l+1]<heights[r-1] and (l+1)!=(r-1):
                    r-=1
                else:
                    l+=1
        return max_area