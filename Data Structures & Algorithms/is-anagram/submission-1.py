class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return self.get_chars(s) == self.get_chars(t)

    def get_chars(self, s) -> dict[int]:
        string_chars = dict()
        for character in s:
            try:
                string_chars[character] += 1
            except KeyError:
                string_chars[character] = 1
        return string_chars