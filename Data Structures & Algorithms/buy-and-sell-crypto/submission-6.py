class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l , r = 0 , 1
        max = 0
        while r < len(prices):
            diff  = prices[r] - prices[l]
            if diff > max:
                max = diff
            elif diff <= 0:
                l = r
            r += 1
        return max
