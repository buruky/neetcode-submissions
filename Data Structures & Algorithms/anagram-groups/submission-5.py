class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tempDic = defaultdict(list)
        # if len(strs) <= 1:
        #     return newList.append(strs)
        for item in strs:
            tmp = tuple(sorted(item))
            tempDic[tmp].append(item)

        return list(tempDic.values())
        
            
                

        
