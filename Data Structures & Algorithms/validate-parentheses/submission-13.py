class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {
            '}': '{',
            ']': '[',
            ')': '('
        }
        for i in s:
            if i in pairs.values():
                stack.append(i)
            elif not stack or pairs[i] != stack.pop():
                return False
        
        
        return True if not stack else False