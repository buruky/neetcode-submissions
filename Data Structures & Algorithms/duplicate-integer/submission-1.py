class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = set()
        booly = False 
        for num in nums:
            if num in dupe:
                booly = True
            else:
                dupe.add(num)
        return booly