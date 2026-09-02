class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        result = {}
        for s in strs:
            sortedS = "".join(sorted(s))
            if sortedS in result:
                result[sortedS].append(s)
            else: 
                result[sortedS] = []
                result[sortedS].append(s)

        return list(result.values())