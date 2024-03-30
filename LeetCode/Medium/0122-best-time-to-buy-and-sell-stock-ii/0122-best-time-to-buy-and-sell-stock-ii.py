class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        sum_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            sum_profit += profit
            if profit > 0:
                min_price = price
        
        return sum_profit