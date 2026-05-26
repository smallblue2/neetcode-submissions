class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non_unique = set()
        for num in nums:
            if num in non_unique:
                return True
            non_unique.add(num)
        return False