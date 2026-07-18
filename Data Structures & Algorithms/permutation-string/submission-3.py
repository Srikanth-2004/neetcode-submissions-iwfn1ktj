class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1)>len(s2):
            return False
        i,j = 0,len(s1)-1
        s1_count = Counter(s1)
        s2_count = Counter(s2[i:j+1])
        while j < len(s2):
            if s1_count == s2_count:
                return True
            else:
                s2_count[s2[i]] -= 1
                if s2_count[s2[i]]==0:
                    s2_count.pop(s2[i])
                i+=1
                j+=1
                if j==len(s2):
                    break
                s2_count[s2[j]] += 1
        return False