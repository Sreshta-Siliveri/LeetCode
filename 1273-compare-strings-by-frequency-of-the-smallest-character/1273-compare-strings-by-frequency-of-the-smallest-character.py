class Solution:
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:
        def f(s: str) -> int:
            smallest_char = min(s)  # Find the lexicographically smallest character
            return s.count(smallest_char)  # Count how many times it appears in the string
        
        # Precompute frequencies for all words
        word_freqs = [f(word) for word in words]
        word_freqs.sort()  # Sort the frequencies of words for efficient comparison
        
        # For each query, find how many word frequencies are greater than the query's frequency
        result = []
        for query in queries:
            query_freq = f(query)  # Get f(query)
            # Use binary search to find the position where query_freq could fit
            # in the sorted word_freqs list such that all elements to the right are greater.
            count_greater = len(word_freqs) - bisect.bisect_right(word_freqs, query_freq)
            result.append(count_greater)
        
        return result