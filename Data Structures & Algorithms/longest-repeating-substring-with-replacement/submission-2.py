"""

Each iteration we need:

k < window length - most frequent char

"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counts = [0] * 26
        base = ord('A')

        longest = 0

        l = 0
        r = 0
        while r < len(s):
            new_char = ord(s[r]) - base
            counts[new_char] += 1

            while l <= r and k < (1 + r - l) - max(counts):
                old_char = ord(s[l]) - base
                #print(f"Used up all spares, kicking out '{s[l]}'")
                counts[old_char] -= 1
                l += 1
            
            longest = max(longest, 1 + r - l)
            r += 1
        
        return longest

            