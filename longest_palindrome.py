import re

class Solution:

    def isPalindrome(self, s: str) -> bool:
        pattern = re.compile('[\W_]+')
        s = pattern.sub('', s)
        s = s.lower()

        mid = len(s) // 2
        i = 0
        n = len(s)
        while i < mid:
            if s[i] != s[n-1-i]:
                return False
            i = i + 1
        return True

    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        i = 0
        maxLength = 0
        subString = ""
        while i < n:
            j = n
            while j > i:
                if (self.isPalindrome(s[i:j])):
                    if len(s[i:j]) > maxLength:
                        maxLength = len(s[i:j])
                        subString = s[i:j]
                j = j - 1
            i = i + 1
        return subString


if __name__ == "__main__":
    s = Solution()
    print(s.longestPalindrome("babad"))
