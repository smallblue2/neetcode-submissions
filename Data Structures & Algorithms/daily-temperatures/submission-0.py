class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        out = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            peek = None
            if stack:
                peek = stack[-1]
            while peek and peek[1] < t:
                current = stack.pop()
                out[current[0]] = i - current[0]
                if stack:
                    peek = stack[-1]
                else:
                    peek = None
            stack.append((i, t))
        return out
