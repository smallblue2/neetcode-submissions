class Solution:
    def assess(self, data, target, action):
        if data.get(target, None) is None:
            data[target] = 0
        data[target] = action(data[target])

    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = dict()
        for letter in s:
            self.assess(count, letter, lambda x: x + 1)
 
        for letter in t:
            self.assess(count, letter, lambda x: x - 1)

        for v in count.values():
            if v != 0:
                return False
        return True