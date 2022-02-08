from typing import List


class Solution:

    def sortedSquares(self, nums: List[int]) -> List[int]:
        squared = [pow(n, 2) for n in nums]
        i, n = 1, len(nums)
        while i < n:
            j = i
            while j > 0:
                if squared[j] < squared[j-1]:
                    temp = squared[j-1]
                    squared[j-1] = squared[j]
                    squared[j] = temp
                j = j - 1 
            i = i + 1
        return squared
