class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = prices[0]
        max_profit = 0
        for day in prices:
            if day < min_buy:
                min_buy = day
            if day - min_buy > max_profit:
                max_profit = day - min_buy
        return max_profit
