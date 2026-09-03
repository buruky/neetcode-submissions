class Solution:
    def isValid(self, s: str) -> bool:
        closed = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }
        stack = []

        for i in s:
            if i == "{" or i == "[" or i == "(":
                stack.append(i)
            elif not stack or closed[i] != stack.pop():
                return False
        return True if not stack else False
             
