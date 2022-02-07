import re
# class Solution:

#     def isPalindrome(self, s: str) -> bool:
#         n = len(s)
#         for i in range(len(s) // 2):
#             if s[i] != s[n-1-i]:
#                 return False
#         return True


#     def longestPalindrome(self, s: str) -> str:
#         self.isPalindrome(s)


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
        

if __name__ == "__main__":
    s = Solution()
    print(s.isPalindrome("A man, a plan, a canal: Panama"))
