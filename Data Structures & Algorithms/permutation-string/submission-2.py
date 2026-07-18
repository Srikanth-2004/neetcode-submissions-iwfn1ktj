class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        i,j=0,len(s1)-1
        while j<len(s2):
            if sorted(s1) == sorted(s2[i:j+1]):
                return True
            j+=1
            i+=1
        return False