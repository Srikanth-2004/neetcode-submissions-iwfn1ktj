class Solution:
    def rob(self, nums: List[int]) -> int:

        def helper(nums):
            r1,r2 = 0,0
            for n in nums:
                newrob = max(r1+n,r2)
                r1 = r2
                r2 = newrob
            return r2
        
        if len(nums)<2:
            return nums[0]


        return max(helper(nums[1:]),helper(nums[:-1]))
