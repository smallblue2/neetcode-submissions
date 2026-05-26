class Solution:
    def maxArea(self, heights: List[int]) -> int:
        return self.recurseAndFind(heights, 0, (len(heights) - 1))

    def recurseAndFind(self, heights, idx, idy):
        length = min(heights[idx], heights[idy])
        width = idy - idx
        area = length * width
        if (idx == idy):
            return area
        option1 = self.recurseAndFind(heights, idx + 1, idy)
        option2 = self.recurseAndFind(heights, idx, idy - 1)
        return max(area, option1, option2)

"""
Two points

[ 1 8 3 5 9 8 2 7 ]
    ^           ^

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