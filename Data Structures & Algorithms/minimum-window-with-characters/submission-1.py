class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s:
            return ""
        
        need = Counter(t)
        missing = len(t)   # total chars we still need
        left = start = end = 0
        
        for right, ch in enumerate(s, 1):  # right is 1-based
            if need[ch] > 0:
                missing -= 1
            need[ch] -= 1
            
            # when we have a valid window
            if missing == 0:
                # shrink from left
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if end == 0 or right - left < end - start:
                    start, end = left, right
                
                # move left pointer to search for next window
                need[s[left]] += 1
                missing += 1
                left += 1
        
        return s[start:end]