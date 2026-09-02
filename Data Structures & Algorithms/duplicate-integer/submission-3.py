class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        if len(nums) <= 1:
            return False
        temp = nums[0]
        for i in range(1, len(nums)): 
            if temp == nums[i]:
                return True
            else:
                temp = nums[i]



        return False
        