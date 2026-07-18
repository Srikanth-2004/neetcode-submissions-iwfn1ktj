class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        i,j = 0,0
        length = 0
        maps = defaultdict(int)
        while j<len(s):
            maps[s[j]] += 1
            if s[j] in maps:
                if (j-i+1)-max(maps.values()) <= k:
                    length = max(j-i+1,length)
                else:
                    maps[s[i]]-=1
                    i+=1
            j+=1
        return length