from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0
        
        # Initialize variables for the two transactions
        first_buy = float('-inf')  # Buying on day 1 (first transaction)
        first_sell = 0  # Selling on day 1 (first transaction)
        second_buy = float('-inf')  # Buying for second transaction
        second_sell = 0  # Selling for second transaction
        
        for price in prices:
            # Update for the first transaction (buy/sell)
            first_buy = max(first_buy, -price)  # Max of not buying today or buying today at the current price
            first_sell = max(first_sell, first_buy + price)  # Max of not selling today or selling today
            
            # Update for the second transaction (buy/sell)
            second_buy = max(second_buy, first_sell - price)  # Max of not buying today or buying today after first transaction
            second_sell = max(second_sell, second_buy + price)  # Max of not selling today or selling today after second buy
        
        return second_sell
