class Solution:
    def isPalindrome(self, s: str) -> bool:

        alphanum = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
        clean = ""
        for c in s:
            if c not in alphanum:
                continue
            clean += c.lower()

        i = 0
        j = len(clean) - 1
        while i < j:
            if clean[i] != clean[j]:
                return False
            i += 1
            j -= 1
        
        return True
        