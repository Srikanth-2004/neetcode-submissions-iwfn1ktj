class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            comp = target - numbers[i]
            l,r = i,len(numbers)-1
            while l<=r:
                mid = (l+r)//2
                if numbers[mid]>comp:
                    r-=1
                elif numbers[mid]<comp:
                    l+=1
                elif numbers[mid]==comp:
                    return [i+1,mid+1]