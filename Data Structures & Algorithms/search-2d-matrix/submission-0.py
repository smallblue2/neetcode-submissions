class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if matrix == [[]]:
            return False
        # First, find the correct row (m)
        first, last = 0, len(matrix) - 1
        pivot = 0
    
        while first <= last:
            pivot = (first + last) // 2
            floor = matrix[pivot][0]
            ceil = matrix[pivot][-1]
    
            if floor > target:
                last = pivot - 1
            elif ceil < target:
                first = pivot + 1
            else:
                break
    
        in_row = matrix[pivot]
        # Another binary search, but now within a single array
        first, last = 0, len(in_row) - 1
        pivot = 0
    
        while first <= last:
            pivot = (first + last) // 2
    
            if in_row[pivot] < target:
                first = pivot + 1
            elif in_row[pivot] > target:
                last = pivot - 1
            else:
                break
    
        return in_row[pivot] == target
    