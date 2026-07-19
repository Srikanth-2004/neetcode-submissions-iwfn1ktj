class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        i,j = 0,k-1
        while j<len(nums):
            maxed = max(nums[i:j+1])
            res.append(maxed)
            i+=1
            j+=1
        return res