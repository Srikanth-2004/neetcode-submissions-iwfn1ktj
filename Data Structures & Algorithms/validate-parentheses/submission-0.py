class Solution:
    def isValid(self, s: str) -> bool:
        chars = {")":"(","]":"[","}":"{"}
        stack = []
        for char in s:
            if char in '({[':
                stack.append(char)
            else:
                if not stack or stack[-1]!=chars[char]:
                    return False
                stack.pop()
        return not stack