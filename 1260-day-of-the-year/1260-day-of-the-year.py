class Solution:
    def dayOfYear(self, date: str) -> int:
        # Parse the year, month, and day from the input string
        year, month, day = map(int, date.split('-'))
        
        # Days in each month for a non-leap year
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        
        # Check if the year is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            days_in_month[2] = 29
        
        # Sum up the days from previous months and add the current day
        return sum(days_in_month[:month]) + day
        