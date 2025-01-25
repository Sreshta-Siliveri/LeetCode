class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel_days = set(days)
        last_day = days[-1]
        
        # Initialize dp array for all days up to the last travel day
        dp = [0] * (last_day + 1)
        
        for i in range(1, last_day + 1):
            if i not in travel_days:
                dp[i] = dp[i - 1]  # No travel cost for non-travel days
            else:
                # Calculate the minimum cost among the three ticket options
                dp[i] = min(
                    dp[i - 1] + costs[0],  # 1-day pass
                    dp[max(0, i - 7)] + costs[1],  # 7-day pass
                    dp[max(0, i - 30)] + costs[2]  # 30-day pass
                )
        
        return dp[last_day]