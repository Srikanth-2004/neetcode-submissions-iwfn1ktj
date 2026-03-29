class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t=="":
            return ""
        count, win = {},{}
        for c in t:
            count[c] = 1 + count.get(c,0)
        
        have,need = 0,len(count)
        res, reslen = [-1,-1],float('inf')
        l = 0

        for r in range(len(s)):
            c = s[r]
            win[c] = 1 + win.get(c,0)
            
            if c in count and win[c]==count[c]:
                have+=1
            
            while have == need:
                if (r-l+1) < reslen:
                    res = [l,r]
                    reslen = r-l+1
                win[s[l]]-=1
                if s[l] in count and win[s[l]] < count[s[l]]:
                    have -= 1
                l+=1
        l,r = res
        return s[l:r+1] if reslen != float('inf') else ""