class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max = 0
        l, r = 0, 1
        while r < len(prices):
            diff = prices[r] - prices[l]
            if diff <= 0:
                l = r
            elif diff > max:
                max = diff
            r += 1
        return max