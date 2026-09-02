
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max = 1
        nums.sort()
        currNum = nums[0]
        currMax = 1
        for i in range(1, len(nums)):
            if nums[i] == currNum + 1:
                currMax = currMax + 1
                if currMax > max:
                    max = currMax
            elif nums[i] != currNum: 
                currMax = 1
            currNum = nums[i]


        

        return max
            
