class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i,j = 0,len(nums)-1
        while i<=j:
            k = (i+j)//2
            if nums[k]==target:
                return k
            elif nums[i] <= nums[k]:
                if nums[i] <= target < nums[k]:
                    j = k-1
                else:
                    i = k+1
            else:
                if nums[k] < target <= nums[j]:
                    i = k+1
                else:
                    j = k-1
        return -1