class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        current_vowel_count = 0
        
        # Initial vowel count for the first window of size k
        for i in range(k):
            if s[i] in vowels:
                current_vowel_count += 1
        
        max_vowels = current_vowel_count
        
        # Slide the window over the string
        for i in range(k, len(s)):
            # Slide the window: remove the character going out of the window
            if s[i - k] in vowels:
                current_vowel_count -= 1
            # Add the character coming into the window
            if s[i] in vowels:
                current_vowel_count += 1
            # Update max vowels found
            max_vowels = max(max_vowels, current_vowel_count)
        
        return max_vowels