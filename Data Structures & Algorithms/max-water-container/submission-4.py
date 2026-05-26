class Solution:
    def maxArea(self, heights: List[int]) -> int:
        index_x = 0
        index_y = len(heights) - 1

        max_area = 0
        while index_y != index_x:
            height = min(heights[index_x], heights[index_y])
            width = index_y - index_x
            area = height * width

            max_area = max(area, max_area)

            if heights[index_x] > heights[index_y]:
                index_y -= 1
            else:
                index_x += 1

        return max_area





"""
[1,7,2,5,12,3,500,500,7,8,4,7,3,6]
               ^   ^   

[ 1 1 1 1 1 1 1 8 8 ]
                ^ ^

Two points

[ 1 8 3 5 9 8 2 7 ]
  ^             ^

[heightsargest ... Smallest]
(V, i)

A = heights * W
heights = min(bar1, bar2)
W = How far apart they are

n^2 different areas

Problems:
 - The furthest away
 - The tallest

Base case:
 - idx, idy == len(heights) - 1
 - idx, idy == 0


# Assume idx is 0, idy is len(heights) - 1
def findBiggestArea(heights, idx=0, idy=(len(heights) - 1)):
    length = min(heights[idx], heights[idy])
    width = idy - idx
    area = length * width
    if (idx == idy):
        return area
    option1 = findBiggestArea(heights, idx + 1, idy)
    option2 = findBiggestArea(heights, idx, idy + 1)
    return max(area, option1, option2)
"""