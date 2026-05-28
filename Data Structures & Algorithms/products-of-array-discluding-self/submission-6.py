class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        zeroCount = 0

        product = 1
        for n in nums:
            if n == 0:
                zeroCount += 1
                continue
            product *= n
        
        out = []
        for n in nums:
            if zeroCount > 1:
                out.append(0)
            elif n == 0:
                out.append(product)
            else:
                if zeroCount > 0:
                    out.append(0)
                else:
                    out.append(product // n)
        
        return out


        
