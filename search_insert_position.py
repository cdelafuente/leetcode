from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                start = mid + 1
            else:
                end = mid - 1

        idx = mid
        if target < nums[idx]:
            idx = 0 if idx - 1 < 0 else idx - 1
        if target > nums[idx]:
            idx = idx + 1
        return idx
    

        

if __name__ == "__main__":
    s = Solution()
    # print(s.searchInsert(nums=[1,3,5,6], target=5)) # 2
    # print(s.searchInsert(nums=[1,3,5,6], target=2)) # 1
    # print(s.searchInsert(nums=[1,3,5,6], target=7)) # 4
    # print(s.searchInsert(nums=[1,3], target=2))     # 1
    # print(s.searchInsert(nums=[1,3,5,6], target=0)) # 0
    # print(s.searchInsert(nums=[2,5], target=1))     # 0
    print(s.searchInsert(nums=[-1,3,5,6], target=0))     # 0