class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = [[p, s] for p,s in zip(position, speed)] #O(n)
        combined.sort(key=lambda x: x[0]) #O(nlogn)
        convoys = 0
        
        stack = []
        i = len(combined) - 1
        while i >= 0:
            atime = (target - combined[i][0]) / combined[i][1]
            if not stack: # First Convoy
                convoys += 1
                stack.append(atime)
            elif atime > stack[-1]: # Faster, join the convoy
                stack.append(atime)
            i -= 1
        
        return len(stack)