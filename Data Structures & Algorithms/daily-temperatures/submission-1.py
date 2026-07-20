class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        output = [0]*n
        stack = []
        for i in range(n):
            while stack and stack[-1][0] < temperatures[i]:
                temp,j = stack.pop()
                output[j] = i-j
            stack.append([temperatures[i],i])
        return output