class Solution:
    def convertTime(self, current: str, correct: str) -> int:
        def time_to_minutes(time: str) -> int:
            hours, minutes = map(int, time.split(":"))
            return hours * 60 + minutes
        
        # Calculate the difference in minutes
        current_minutes = time_to_minutes(current)
        correct_minutes = time_to_minutes(correct)
        difference = correct_minutes - current_minutes
        
        # Greedy approach to minimize operations
        operations = 0
        for step in [60, 15, 5, 1]:
            operations += difference // step
            difference %= step
        
        return operations