class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        res = [1] * ln

        # Build prefix
        prefix = 1
        i = 0
        while i < ln:
            res[i] *= prefix
            prefix *= nums[i]
            i += 1
        
        # Build suffix
        suffix = 1
        i = ln - 1
        while i >= 0:
            res[i] *= suffix
            suffix *= nums[i]
            i -= 1
        
        return res

