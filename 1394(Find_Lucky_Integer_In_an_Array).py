from typing import List

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = [0] * 501  # Since 1 <= arr[i] <= 500

        # Count frequency of each number
        for num in arr:
            freq[num] += 1

        # Search for the largest lucky number
        for i in range(500, 0, -1):
            if freq[i] == i:
                return i

        return -1
