"""

Area = min(val2, val1) * (idx2 - idx1)

Ideally want the furthest away with height
Keep the height, move the smallest in
"""

class Solution:
    def maxArea(self, heights: List[int]) -> int:
        max_area = 0

        i = 0
        j = len(heights) - 1
        while i < j:
            if heights[i] == 0 or heights[j] == 0:
                area = 0
            else:
                area = min(heights[i], heights[j]) * (j - i)
            print(f"At {i}, {j}; area = {area}")

            if area > max_area:
                max_area = area
            
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return max_area

