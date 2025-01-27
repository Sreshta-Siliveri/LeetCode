class Solution:
    def longestPalindrome(self, s: str) -> int:
        char_count = Counter(s)  # Count the occurrences of each character
        length = 0
        odd_found = False  # Track if an odd count character is found

        for count in char_count.values():
            if count % 2 == 0:
                length += count  # Use all even counts
            else:
                length += count - 1  # Use the largest even part
                odd_found = True  # Track the presence of odd counts

        # If there's any odd count, one character can be used in the middle
        if odd_found:
            length += 1

        return length
