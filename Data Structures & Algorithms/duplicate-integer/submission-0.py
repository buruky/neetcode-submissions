class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dupe = dict()
        booly = False 
        for num in nums:
            if num in dupe:
                booly = True
            else:
                dupe.update({num : 1})
        return booly