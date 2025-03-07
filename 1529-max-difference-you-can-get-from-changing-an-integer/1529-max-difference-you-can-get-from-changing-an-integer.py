class Solution:
    def maxDiff(self, num: int) -> int:
        num_str = str(num)

        # Maximum number transformation: Replace the first non-9 digit with 9
        for digit in num_str:
            if digit != '9':
                max_num = int(num_str.replace(digit, '9'))
                break
        else:  # If all digits are '9', then num is already the largest possible
            max_num = num

        # Minimum number transformation:
        # - If the first digit is not '1', replace it with '1' (to avoid leading zeros)
        # - Otherwise, replace the first non-0, non-1 digit with '0'
        if num_str[0] != '1':
            min_num = int(num_str.replace(num_str[0], '1'))
        else:
            for digit in num_str[1:]:
                if digit not in ('0', '1'):
                    min_num = int(num_str.replace(digit, '0'))
                    break
            else:  # If no such replacement was needed, num is already the smallest possible
                min_num = num

        return max_num - min_num
