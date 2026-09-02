class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # sets whole list to 1's
        res = [1] * (len(nums))
        # fills result array wuth all of the pre-multiplications
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        # gives a default post mult for the last 
        # number since the products is just all of the previous number times 1
        postfix = 1
        # multiplies all of the pre by the post 
        for i in range(len(nums) - 1, -1, -1):
            # whatever the pre-mult times the post-mult
            res[i] *= postfix
            # sets the post mult to be itself times the latest number in nums.
            postfix *= nums[i]
        return res