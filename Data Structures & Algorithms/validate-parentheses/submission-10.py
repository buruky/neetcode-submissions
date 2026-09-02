class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in range(len(s)):
            if s[i] in pairs.values():
                stack.append(s[i])
                print(stack)
            elif not stack or pairs[s[i]] != stack.pop():
                return False
        
        
        return True if not stack else False