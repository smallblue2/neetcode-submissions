class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        char_set = {}

        for char in s:
            char_set[char] = char_set.get(char, 0) + 1
        
        for char in t:
            char_set[char] = char_set.get(char, 0) - 1
        
        for value in char_set.values():
            if value != 0:
                return False
        return True