class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        out = []
        nums.sort() # O(n logn)

        base = 0
        while base < len(nums) - 2: # O(n - 2)
            if nums[base] > 0: # Impossible scenario, we're finished
                print("Early exit")
                break
            if base > 0 and nums[base] == nums[base - 1]: # Skip duplicate base nums
                print(f"Skipping dupe ({base}: {nums[base]})")
                base += 1
                continue

            i = base + 1
            j = len(nums) - 1
            while i < j: # O(n)
                num = nums[base] + nums[i] + nums[j]
                if num == 0:
                    out.append([nums[base], nums[i], nums[j]]) 
                    i += 1
                    j -= 1

                    # Skip pointer dupes
                    while i < j and nums[i] == nums[i - 1]:
                        i += 1
                    while i < j and nums[j] == nums[j + 1]:
                        j -= 1

                    continue
                if num < 0:
                    i += 1
                else:
                    j -= 1
            base += 1
        
        return out

# O(n logn + (n - 2) * n)

