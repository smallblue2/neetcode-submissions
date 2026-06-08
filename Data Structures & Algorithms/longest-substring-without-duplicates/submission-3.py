class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        biggest = 0
        l = 0
        r = 0
        while r < len(s):
            if s[r] in charset:
                print(f"Duplicate: '{s[r]}'")
                while l <= r and s[r] in charset: # Don't go past r
                    print(f"Removed: '{s[l]}'")
                    charset.remove(s[l])
                    l += 1
            print(f"Added: '{s[r]}'")
            charset.add(s[r])
            biggest = max(biggest, 1 + r - l)
            r += 1
        
        return biggest