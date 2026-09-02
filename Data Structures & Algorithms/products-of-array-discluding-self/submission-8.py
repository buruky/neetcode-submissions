import math
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        zCount = 0
        for n in nums:
            if n == 0:
                zCount += 1
                if zCount == 2:
                    return [0] * len(nums)
            else:
                prod = n*prod
        
        res = []
        for n in nums:
            if zCount == 1:
                newProd = 0
                if n == 0:
                    newProd = prod
            else:
                newProd = prod//n
            res.append(newProd)
        return res
        