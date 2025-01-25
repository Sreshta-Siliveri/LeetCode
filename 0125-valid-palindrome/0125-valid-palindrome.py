class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_s = ''.join(c.lower() for c in s if c.isalnum())
        
        # Step 2: Check if the filtered string is a palindrome
        return filtered_s == filtered_s[::-1]