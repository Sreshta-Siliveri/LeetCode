from typing import List

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        for row in image:
            # Reverse the row and invert it in one pass
            for i in range((len(row) + 1) // 2):
                # Swap and invert values using XOR
                row[i], row[-i - 1] = row[-i - 1] ^ 1, row[i] ^ 1
        return image
