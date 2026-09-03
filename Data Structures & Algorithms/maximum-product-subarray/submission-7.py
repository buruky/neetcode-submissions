class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        res = max(nums)
        curMax, curMin = 1, 1

        for n in nums:
            temp = curMin
            curMin = min(n, curMin * n, curMax * n)
            curMax = max(n, temp * n, curMax * n)
            res = max(curMax, res)
        return res

