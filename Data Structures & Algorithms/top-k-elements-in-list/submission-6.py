"""


"""
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = defaultdict(lambda: 0)

        highest = 0
        for num in nums:
            cur = freq_map[num] + 1 
            freq_map[num] = cur
            if cur > highest:
                highest = cur
        
        freq_list = [[] for i in range(highest)]
        for num, freq in freq_map.items():
            print(num, freq)
            freq_list[freq - 1].append(num)
        
        output = []
        while highest >= 0 and len(output) < k:
            current = freq_list[highest - 1]
            if len(current) != 0:
                output += current
            highest -= 1
        print(freq_list)
        return output[len(output) - k:]
