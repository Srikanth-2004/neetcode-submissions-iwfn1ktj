class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp in hash_table:
                return [hash_table[comp],i]
            hash_table[nums[i]] = i