class Solution:
    def shortestPalindrome(self, s: str) -> str:
        rev_s = s[::-1]
        # Create a new string combining s and its reverse
        new_s = s + "#" + rev_s

        # Find the longest prefix of `s` which is also a suffix of `rev_s`
        lps = [0] * len(new_s)
        j = 0  # length of previous longest prefix suffix

        for i in range(1, len(new_s)):
            while j > 0 and new_s[i] != new_s[j]:
                j = lps[j - 1]
            if new_s[i] == new_s[j]:
                j += 1
            lps[i] = j

        # Calculate the characters that need to be added
        to_add = rev_s[:len(s) - lps[-1]]
        return to_add + s