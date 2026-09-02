class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        k = i = 0  
        while i < n:
            chars[k] = chars[i]
            k += 1
            j = i + 1
            while j < n and chars[j] == chars[i]:
                j += 1
            jLen = str(j - i)
            if j - i > 1:
                for c in jLen:
                    chars[k] = c
                    k += 1
            i = j
        return k


