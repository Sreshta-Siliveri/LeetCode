class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        vowels = set("aeiou")
        count = 0

        for i in range(len(word)):
            vowel_set = set()
            for j in range(i, len(word)):
                if word[j] in vowels:
                    vowel_set.add(word[j])
                    if len(vowel_set) == 5:  # All vowels are present
                        count += 1
                else:
                    break  # Stop if we encounter a non-vowel

        return count