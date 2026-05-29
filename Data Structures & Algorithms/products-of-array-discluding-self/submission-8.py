class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ln = len(nums)
        pref = [0] * ln
        suf = [0] * ln
        out = [0] * ln

        # Build prefix
        prefix = 1
        i = 0
        while i < ln:
            pref[i] = prefix
            prefix *= nums[i]
            i += 1
        
        # Build suffix
        suffix = 1
        i = ln - 1
        while i >= 0:
            suf[i] = suffix
            suffix *= nums[i]
            i -= 1
        
        return [s * p for s, p in zip(suf, pref)]

