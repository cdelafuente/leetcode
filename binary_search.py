from typing import List


class Solution:
    def binarySearch(self, nums: List[int], target: int, start: int, end: int) -> int:
        if start > end or end < start:
            return -1
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif target < nums[mid]:
            return self.binarySearch(nums, target, start, mid-1)
        else:
            return self.binarySearch(nums, target, mid+1, end)
                

    def search(self, nums: List[int], target: int) -> int:
        return self.binarySearch(nums, target, 0, len(nums)-1)


if __name__ == "__main__":
    s = Solution()
    # print(s.search(nums=[-1,0,3,5,9,12], target=9))
    print(s.search(nums=[-1,0,3,5,9,12], target=2))
    print(s.search(nums=[-1,0,3,5,9,12], target=13))
    print(s.search(nums=[-1,0,3,5,9,12], target=12))
