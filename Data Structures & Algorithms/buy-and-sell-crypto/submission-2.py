class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l,r = 0,1
        maxed = 0
        while r<len(prices):
            if prices[l]>prices[r]:
                l = r
                r += 1
            else:
                maxed = max(maxed,prices[r]-prices[l])
                r+=1
        return maxed
