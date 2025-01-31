from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize total profit to 0
        total_profit = 0
        
        # Iterate through the prices and calculate the profit
        for i in range(1, len(prices)):
            if prices[i] > prices[i - 1]:
                # If the current price is greater than the previous, we make a profit
                total_profit += prices[i] - prices[i - 1]
        
        return total_profit
