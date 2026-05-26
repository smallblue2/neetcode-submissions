"""

    First find pivot point (binary search), create slice, search (binary search)

    [3,4,5,6,7,1,2] -> mid > upper, RIGHT
     ^     ^     ^
    [7,1,2,3,4,5,6] -> mid < lower, LEFT
     ^ ^     
     ^
    [4,5,6,1,2,3,4] -> left < mid < right -> FOUND

    [1,2,3,4,5,6]
     ^   ^     ^

    [3,4,5,6,1,2]
             ^^ ^

    Binary search, go to the right partition if it is less than pivot

"""

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        wrap = self.find_minimum(nums)

        lower, upper = 0, len(nums) - 1

        while lower <= upper:
            mid = (upper + lower) // 2

            # [4,5,6,1,2,3]
            real_mid = (mid + wrap) % len(nums)

            if nums[real_mid] == target:
                return real_mid
            elif nums[real_mid] < target:
                lower = mid + 1
            else:
                upper = mid - 1
        
        return -1



    def find_minimum(self, nums: List[int]) -> int:
        # Binary search
        lower, upper = 0, len(nums) - 1

        while lower < upper:
            mid = (lower + upper) // 2

            if nums[mid] > nums[upper]:
                lower = mid + 1
            else:
                upper = mid
            
        return lower
