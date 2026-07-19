class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s)<len(t):
            return ""
        res = [-1,-1]
        have = 0
        t_count = Counter(t)
        s_count = defaultdict(int)
        need = len(t_count)
        i=0
        min_len = float('inf')
        for j in range(len(s)):
            s_count[s[j]]+=1
            if s[j] in t_count and s_count[s[j]] == t_count[s[j]]:
                have += 1
            while have == need:
                if (j-i+1) < min_len:
                    min_len = j-i+1
                    res = [i,j]
                s_count[s[i]]-=1
                if s[i] in t_count and s_count[s[i]] < t_count[s[i]]:
                    have -= 1
                i+=1
        l,r = res
        return s[l:r+1] if min_len!=float('inf') else ""