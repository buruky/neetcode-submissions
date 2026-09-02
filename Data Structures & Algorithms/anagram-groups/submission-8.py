class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if len(strs) <= 1:
            return [strs]
        result = defaultdict(list)
        for s in strs:
            sortedS = "".join(sorted(s))
            result[sortedS].append(s)

        return list(result.values())