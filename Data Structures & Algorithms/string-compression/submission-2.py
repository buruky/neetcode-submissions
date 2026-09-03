class Solution:
    def compress(self, chars: List[str]) -> int:
        n = len(chars)
        cnt = 0 
        l = 0

        while l < n:
            chars[cnt] = chars[l]
            cnt += 1
            r = l + 1
            while r < n and chars[r] == chars[l]:
                r += 1
            jLen = str(r - l)
            if r - l > 1:
                for c in jLen:
                    chars[cnt] = c
                    cnt += 1
            l = r
        return cnt
                
                

