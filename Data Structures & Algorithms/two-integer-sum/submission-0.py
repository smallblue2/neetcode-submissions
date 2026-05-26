class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        memory = dict()

        for i, num in enumerate(nums):
            difference = target - num
            if num in memory:
                return [memory[num], i]
            memory[difference] = i
            print(memory)
        
        return [0, 0]
