def isBadVersion(version: int) -> bool:
    if version >= 6:
        return True
    return False

class Solution:
    def firstBadVersion(self, n: int) -> int:
        start = 1
        end = n
        bad = -1
        while start <= end:
            middle = (start + end) // 2
            if isBadVersion(middle):
                bad = middle
                end = middle - 1
            else:
                start = middle + 1
        return bad
            

if __name__ == "__main__":
    s = Solution()
    print(s.firstBadVersion(5))


'''
1 2 3 4 5
f f t t t
'''