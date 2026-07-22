class Solution:
    def findMin(self, nums: List[int]) -> int:
        i,j = 0,len(nums)-1
        while i<j:
            k = (i+j)//2
            if nums[k]>nums[j]:
                i = k+1
            else:
                j = k
        return nums[i]