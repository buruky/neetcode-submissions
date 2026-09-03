class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, curr, sums):
            if target == sums:
                res.append(curr.copy())
                return
            if i >= len(nums) or sums >= target:
                return
            
            curr.append(nums[i])
            dfs(i, curr, sums + nums[i])
            curr.pop()
            dfs(i+1, curr, sums)
        dfs(0,[], 0)
        return res