from typing import List


class Solution:
    
    def containsDuplicate(self, nums: List[int]) -> bool:
        count = {}
        size = len(nums)
        i = 0
        while i < size:
            num = nums[i]
            if num not in count:
                count[num] = 1
            else:
                return True
            i = i + 1
        return False
        