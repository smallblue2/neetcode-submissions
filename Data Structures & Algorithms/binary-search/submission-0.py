class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.binary_search(nums, target)

    def binary_search(self, l, t):
        left, right, = 0, len(l) - 1

        while left <= right:
            pivot = (left + right) // 2

            if l[pivot] == t:
                return pivot
            elif l[pivot] < t:
                left = pivot + 1
            else:
                right = pivot - 1
        
        return -1
