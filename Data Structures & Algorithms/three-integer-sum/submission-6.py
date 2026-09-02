class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums)):
            # Skip duplicates for the first element
            if i > 0 and nums[i] == nums[i-1]:
                continue
            n = nums[i]
            target = -n
            answers = dict()
            for j in range(i + 1, len(nums)):
                m = nums[j]
                
                if m in answers:
                    triplet = [n, answers[m], m]
                    if triplet not in res:
                        res.append(triplet)
                    
                    while j + 1 < len(nums) and nums[j] == nums[j + 1]:
                        j += 1
                else:
                    diff = target - m
                    answers[diff] = m
        return res
        