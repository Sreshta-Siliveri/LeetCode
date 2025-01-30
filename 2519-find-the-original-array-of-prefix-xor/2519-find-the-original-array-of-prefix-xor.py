class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        n = len(pref)
        arr = [0] * n
        
        # The first element of arr is the same as the first element of pref
        arr[0] = pref[0]
        
        # Calculate subsequent elements using the XOR property
        for i in range(1, n):
            arr[i] = pref[i] ^ pref[i - 1]
        
        return arr
