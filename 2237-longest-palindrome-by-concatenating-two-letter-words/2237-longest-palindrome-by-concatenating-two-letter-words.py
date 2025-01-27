class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        word_count = Counter(words)  # Count occurrences of each word
        palindrome_length = 0
        used_middle = False  # Track if we used a middle palindrome word

        for word, count in word_count.items():
            # Case 1: The word is a palindrome itself (e.g., "gg")
            if word[0] == word[1]:
                if count % 2 == 0:
                    palindrome_length += count * 2  # Use all pairs
                else:
                    palindrome_length += (count - 1) * 2  # Use all but one
                    used_middle = True  # Save one for the middle
            # Case 2: The word has a reversed counterpart (e.g., "lc" and "cl")
            else:
                reversed_word = word[::-1]
                if reversed_word in word_count:
                    pairs = min(count, word_count[reversed_word])
                    palindrome_length += pairs * 4  # Each pair contributes 4 characters
                    word_count[reversed_word] = 0  # Avoid double counting

        # Add one palindromic word in the middle if possible
        if used_middle:
            palindrome_length += 2

        return palindrome_length