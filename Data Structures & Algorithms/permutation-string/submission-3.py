class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
            
        base = ord('a')

        # Build permutation fingerprint
        fingerprint = [0] * 26
        for c in s1:
            fingerprint[ord(c) - base] += 1
        fingerprint = tuple(fingerprint)

        lookup = dict()
        lookup[fingerprint] = True

        window_length = len(s1)
        current_fingerprint = [0] * 26
        l = 0
        r = 0
        while r < window_length:
            current_fingerprint[ord(s2[r]) - base] += 1
            r += 1
        
        print(f"l: {l},r: {r}")
        
        while r < len(s2):
            check = tuple(current_fingerprint)
            if lookup.get(check, False):
                return True
            current_fingerprint[ord(s2[l]) - base] -= 1
            current_fingerprint[ord(s2[r]) - base] += 1
            l += 1
            r += 1
        
        check = tuple(current_fingerprint)
        if lookup.get(check, False):
            return True

        return False

        

