"""

For each string, 
fingerprint it via freq count
Compare existing fingerprints
if exists, group
if not, new group + save fingerprint

We need a hashable fingerprint
fixed-size array: strs[i] is constraint to a <= x <= z, lowercase only
Fingerprint can be: list: int[26]
"""

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key = fingerprint, value = dynamic string array
        groups = dict()

        relative = ord('a')
        for s in strs:
            fingerprint = [0] * 26
            for char in s:
                fingerprint[ord(char) - relative] += 1
            fingerprint = tuple(fingerprint)

            group = groups.get(fingerprint, None)
            if group is None:
                group = []
            group.append(s)
            groups[fingerprint] = group

        return [v for v in groups.values()]