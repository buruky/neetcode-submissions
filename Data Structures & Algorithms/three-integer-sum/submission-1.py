class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for first in range(len(nums) - 2):
            if first > 0 and nums[first] == nums[first - 1]:
                continue  # Skip duplicate elements
            
            left, right = first + 1, len(nums) - 1
            while left < right:
                threeSum = nums[first] + nums[left] + nums[right]
                if threeSum == 0:
                    res.append([nums[first], nums[left], nums[right]])
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1    
                    left += 1
                    right -= 1  
                elif threeSum > 0:
                    right -= 1
                else:
                    left += 1
        return res