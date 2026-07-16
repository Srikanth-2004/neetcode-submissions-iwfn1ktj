class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        longest=0
        for i in range(len(nums)):
            length = 1
            if nums[i]-1 in hash_set:
                continue
            while nums[i]+1 in hash_set:
                length+=1
                nums[i]+=1
            longest = max(length,longest)
        return longest