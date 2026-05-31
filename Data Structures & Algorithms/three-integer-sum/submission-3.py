class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = set()
        nums.sort()

        base = 0
        while base < len(nums) - 2:
            i = base + 1
            j = len(nums) - 1
            while i < j:
                num = nums[base] + nums[i] + nums[j]
                if num == 0:
                    out.add((nums[base], nums[i], nums[j])) 
                if num < 0:
                    i += 1
                else:
                    j -= 1
            base += 1
        
        return list(out)

