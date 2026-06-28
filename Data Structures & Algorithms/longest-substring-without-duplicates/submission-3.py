class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        i=0
        result = set()
        longest = 0
        for j in range(n):
            while s[j] in result and i<j:
                result.remove(s[i])
                i+=1
            result.add(s[j])
            longest = max(j-i+1,longest)
        return longest

