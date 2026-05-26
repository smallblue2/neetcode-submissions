class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = {}
        
        for i, val in enumerate(nums):
            seen = memory.get(target - val, None)
            if not seen is None:
                return [seen, i]
            memory[val] = i
        
        return [-1,-1]