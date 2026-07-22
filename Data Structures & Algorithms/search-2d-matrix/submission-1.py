class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows,cols = len(matrix),len(matrix[0])
        top,left = 0,0
        bottom,right = rows-1,cols-1
        while top<=bottom:
            mid = (top+bottom)//2
            if matrix[mid][-1] < target:
                top=mid+1
            elif matrix[mid][0] > target:
                bottom=mid-1
            else:
                break
        if top>bottom:
            return False
        target_row = (top+bottom)//2
        while left<=right:
            mid = (left+right)//2
            if matrix[target_row][mid] < target:
                left=mid+1
            elif matrix[target_row][mid] > target:
                right=mid-1
            else:
                return True
        return False