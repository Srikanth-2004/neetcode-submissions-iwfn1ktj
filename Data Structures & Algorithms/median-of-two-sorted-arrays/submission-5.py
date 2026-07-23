class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        a = nums1
        b = nums2
        if len(a)>len(b):
            a,b=b,a
        total = len(a)+len(b)
        half = total//2
        i,j = 0,len(a)-1
        while True:
            l = (i+j)//2
            r = half-l-2
            aleft = a[l] if l>=0 else float('-inf')
            aright = a[l+1] if l+1 < len(a) else float('inf')
            bleft = b[r] if r>=0 else float('-inf')
            bright = b[r+1] if r+1 < len(b) else float('inf')

            if aleft <= bright and bleft <= aright:
                if total%2:
                    return min(aright,bright)
                return (max(aleft,bleft) + min(aright,bright)) / 2
            elif aleft > bright:
                j = l-1
            else:
                i = l+1 
