class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {')':'(','}':'{',']':'['}
        for char in s:
            if char in '[{(':
                stack.append(char)
            else:
                if not stack:
                    return False
                if maps[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if not stack:
            return True
        else:
            return False