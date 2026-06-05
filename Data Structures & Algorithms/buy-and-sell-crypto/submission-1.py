class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        smallest = prices[0]
        max_profit = 0
        i = 0
        while i < len(prices) - 1:
            print(f"starting on {prices[i]}")
            j = i + 1
            while j < len(prices):
                print(f"scanning forward: {prices[j]}")
                if prices[j] <= smallest: # Found new start point
                    print(f"Found new small value: {prices[j]}")
                    smallest = prices[j]
                    i = j - 1
                    break
                diff = prices[j] - prices[i]
                if diff >= max_profit:
                    max_profit = diff
                    print(f"New max profit found: {max_profit}")
                j += 1
            i += 1
        
        return max_profit