class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        buckets = {}
        base = ord("a")
        

        for string in strs: # O(n) ; n = #strings
            freqs = [0] * 26
            fingerprint = ""
            for char in string: # O(m) ; m = #avg_len_string
                index = ord(char) - base
                freqs[index] += 1
            fingerprint = "".join(
                [chr(freq) for freq in freqs] # O(26)
                ) # O(m)
            bucket = buckets.get(fingerprint, None) # O(1)
            if bucket is None:
                buckets[fingerprint] = [string]
            else:
                bucket.append(string)

        return list(buckets.values()) # O(n)

        # O(n * m + 26 + m + 1 + n)
        # Final: O(n * m)