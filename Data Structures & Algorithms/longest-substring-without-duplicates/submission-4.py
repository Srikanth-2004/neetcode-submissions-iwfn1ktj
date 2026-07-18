class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        n = len(s)
        longest = 0
        visited = set()
        for j in range(n):
            while s[j] in visited and i<j:
                visited.remove(s[i])
                i+=1
            visited.add(s[j])
            longest = max(j-i+1,longest)
        return longest