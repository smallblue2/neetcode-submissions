class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1

        while i < j:
            lower = numbers[i]
            higher = numbers[j]
            if lower + higher == target:
                return [i + 1, j + 1]
            if lower + higher > target:
                j -= 1
            else:
                i += 1