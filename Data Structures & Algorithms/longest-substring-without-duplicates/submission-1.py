class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charset = set()
        max_size = 0
        l = 0
        r = 0
        while r < len(s):
            while s[r] in charset: # Dupe
                charset.remove(s[l]) 
                #print(f"left point: {s[l]}")
                l += 1
            charset.add(s[r])
            max_size = max(1 + r - l, max_size)
            r += 1
        return max_size