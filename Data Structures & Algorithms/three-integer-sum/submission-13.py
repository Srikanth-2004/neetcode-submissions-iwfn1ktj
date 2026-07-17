class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        visited = []
        nums.sort()
        for i in range(len(nums)):
            j = i+1
            k = len(nums)-1
            while j<k:
                if (nums[i]+nums[j]+nums[k]) == 0:
                    if [nums[i],nums[j],nums[k]] not in visited:
                        visited.append([nums[i],nums[j],nums[k]])
                    j+=1
                elif (nums[i]+nums[j]+nums[k]) < 0:
                    j+=1
                elif (nums[i]+nums[j]+nums[k]) > 0:
                    k-=1
        return visited