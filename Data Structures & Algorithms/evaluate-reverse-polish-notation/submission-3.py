class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for val in tokens:
            if val not in ["+","-","*","/"]:
                stack.append(int(val))
            else:
                a = stack.pop()
                b = stack.pop()
                if val=="+":
                    res = a+b
                elif val=="-":
                    res = b-a
                elif val=="*":
                    res = b*a
                elif val=="/":
                    res = int(b/a)
                stack.append(res)
        return stack[-1]