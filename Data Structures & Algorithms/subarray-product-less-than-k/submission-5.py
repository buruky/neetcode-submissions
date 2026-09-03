class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        cnt = 0
        l = 0
        total = 1
        for r in range(len(nums)):
            total *= nums[r]
            while total >= k and l <= r:
                total //= nums[l]
                l += 1
                
            cnt += (r - l + 1)
            r += 1
        return cnt