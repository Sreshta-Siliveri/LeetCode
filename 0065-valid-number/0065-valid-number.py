class Solution:
    def isNumber(self, s: str) -> bool:
        # Regular expression to match valid numbers
        pattern = r'^[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?$'
        # Return True if the string matches the pattern, otherwise False
        return bool(re.match(pattern, s.strip()))