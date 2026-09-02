class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        import queue
        q = queue.Queue()
        for c in s2:
            if c in s1:
                s1 = s1.replace(c, "", 1)
                q.put(c)
            else:
                while not q.empty():
                    p = q.get()
                    if c == p:
                        q.put(p)
                        break
                    else:
                        s1 += p
                pass
            if len(s1) == 0:
                return True
        return False

        ## prev soln
        l = 0
        sLen = len(s1) - 1
        r = sLen
        print(r)
        temp = s1[:]

        while l <= r and r < len(s2) - 1:
            if s2[l] in temp:
                print(f"replace {s2[l]} in {temp}")

                temp = temp.replace(s2[l], "")

                print(f"after replace {temp}")
                l += 1
            else : 
                temp = s1[:]
                l += 1
                r = l + sLen
                #while s2[l] not in temp and r < len(s2) - 1:
                #    l += 1
                #    r += 1
                print(f'fail: l={l} r={r}')
            if len(temp) == 0:
                return True
        return False
        