class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        word_to_index = {word: i for i, word in enumerate(words)}
        result = []

        for i, word in enumerate(words):
            n = len(word)
            for j in range(n + 1):  # Split the word into two parts
                prefix, suffix = word[:j], word[j:]
                
                # Check if prefix is a palindrome and the reverse of the suffix exists in the map
                if self.isPalindrome(prefix):
                    reversed_suffix = suffix[::-1]
                    if reversed_suffix in word_to_index and word_to_index[reversed_suffix] != i:
                        result.append([word_to_index[reversed_suffix], i])

                # Check if suffix is a palindrome and the reverse of the prefix exists in the map
                # Avoid duplicates when j == 0 (entire word is prefix)
                if j != n and self.isPalindrome(suffix):
                    reversed_prefix = prefix[::-1]
                    if reversed_prefix in word_to_index and word_to_index[reversed_prefix] != i:
                        result.append([i, word_to_index[reversed_prefix]])

        return result

    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]