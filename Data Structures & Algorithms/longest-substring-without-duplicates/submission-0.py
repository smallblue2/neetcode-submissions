class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        max_size = 0
        l = 0
        r = 0
        while r < len(s):
            print(f"right point: {s[r]}")
            if s[r] in charset: # Duplicate
                print(f"DUPLICATE, moving left pointer")
                while l <= r: # Continue until
                    charset.remove(s[l]) 
                    print(f"left point: {s[l]}")
                    l += 1
                    if s[l - 1] == s[r]:
                        break
            charset.add(s[r])
            max_size = max(1 + r - l, max_size)
            r += 1
        return max_size

"thisisatest"