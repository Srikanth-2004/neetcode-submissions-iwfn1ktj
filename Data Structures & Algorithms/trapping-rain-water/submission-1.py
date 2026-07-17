class Solution:
    def trap(self, height: List[int]) -> int:
        n = len(height)
        i,j = 0,n-1
        max_l = height[i]
        max_r = height[j]
        area = 0
        while i<j:
            if max_l<=max_r:
                i+=1
                max_l = max(max_l,height[i]) 
                area += max_l - height[i]
            else:
                j-=1
                max_r = max(max_r,height[j])
                area += max_r - height[j]
        return area
