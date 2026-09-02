import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zCount = 0
        for n in nums:
            if n == 0:
                zCount += 1
            else:
                prod = n*prod
        if zCount > 1:
            return [0] * len(nums)
        res = []
        for n in nums:
            if n != 0 and zCount > 0:
                newProd = 0
            elif n != 0:
                newProd = prod // n
            else:
                newProd = prod
            res.append(newProd)
        return res
        