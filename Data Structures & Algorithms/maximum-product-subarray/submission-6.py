class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMin, curMax = 1, 1

        for n in nums:
            temp  = curMax
            curMax = max(n, n * curMin, n * curMax)
            curMin = min(n, n * curMin, n * temp)
            res = max(res, curMax)
        return res