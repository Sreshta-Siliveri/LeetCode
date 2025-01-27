class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left: int, right: int) -> str:
            # Expand as long as the substring is a palindrome
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the palindromic substring
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd-length palindrome centered at i
            odd_palindrome = expandAroundCenter(i, i)
            # Even-length palindrome centered between i and i+1
            even_palindrome = expandAroundCenter(i, i + 1)
            # Update the longest palindrome found so far
            longest = max(longest, odd_palindrome, even_palindrome, key=len)

        return longest
        