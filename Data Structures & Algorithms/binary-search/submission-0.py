class Solution:
    def search(self, nums: List[int], target: int) -> int:
        maxi = len(nums) - 1
        mini = 0

        if maxi == 0 and nums[maxi] == target:
            return 0 
        mid = maxi // 2
        
        while mini <= maxi:
            if target == nums[mid]:
                return mid
            elif target > nums[mid]:
                mini = mid + 1
            else:
                maxi = mid - 1
            mid = (maxi + mini) // 2
        return -1


