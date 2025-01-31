from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the variables for minimum price and maximum profit
        min_price = float('inf')  # Initialize to a very high value
        max_profit = 0  # Initialize profit to 0
        
        # Iterate through the prices
        for price in prices:
            # Update the minimum price encountered so far
            min_price = min(min_price, price)
            
            # Calculate the current profit if selling at the current price
            profit = price - min_price
            
            # Update the maximum profit
            max_profit = max(max_profit, profit)
        
        return max_profit
