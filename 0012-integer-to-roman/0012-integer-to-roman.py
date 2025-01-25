class Solution:
    def intToRoman(self, num: int) -> str:
        values = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), 
            (100, "C"), (90, "XC"), (50, "L"), (40, "XL"), 
            (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), 
            (1, "I")
        ]
        
        result = ""
        
        # Loop through all possible Roman numeral values
        for value, symbol in values:
            # While num is greater than or equal to the current value, subtract it and add the symbol
            while num >= value:
                result += symbol
                num -= value
        
        return result