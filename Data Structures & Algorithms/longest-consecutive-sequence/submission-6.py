"""

[2,20,4,10,3,4,5]

2: 1,3 <- nothing

20: 19,21 <- nothing

4: 3,5 <- nothing

10: 9,11 <- nothing

3: 2,4 <- hit on 2 & 4, max run 3; +2 [2,4]

4: 3,5 <- already encountered

5: 4,6 <- hit on 4, max run 4; +1 [2,5]


runs = [[2,3,4], [8,9,10]]

run = [[2,4], [9,10]]

O(n * m); n = # input, m = # runs

Actually, just find starts of potential runs, and then see how long they are
Need to turn input into map / set for lookups, also reduces duplicates which is good

"""
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
            
        lookup = set()
        for n in nums: # O(n); n = # input
            lookup.add(n)
        
        longest_run = 0
        for n in lookup: # O(n); n = # input
            if (n - 1) in lookup:
                # Not at a start, skip
                continue
            # Guaranteed at a start
            i = n
            current_run = 1
            # The while loop is bounded by the length of the run. 
            # Because we only enter this loop at the start of a sequence,
            # each number is visited by this inner loop at most ONCE across the entire program.
            # Total time complexity remains strictly O(n).
            while (i + 1) in lookup:
                current_run += 1
                i += 1
            if current_run > longest_run:
                longest_run = current_run
        
        return longest_run