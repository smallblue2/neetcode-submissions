class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_set_s = {}
        char_set_t = {}

        pointer = 0
        while (pointer < len(s)):
            char_set_s[s[pointer]] = char_set_s.get(s[pointer], 0) + 1
            char_set_t[t[pointer]] = char_set_t.get(t[pointer], 0) + 1
            pointer += 1

        for value in char_set_s.keys():
            if (not value in char_set_t):
                return False
            if (char_set_s[value] != char_set_t[value]):
                return False

        return True