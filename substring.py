'''
class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxLength = 0
        subString = ""

        while i < len(s):
            end = i
            count = {}

            while end < len(s):
                char = s[end]
                if char not in count:
                    count[char] = 1
                    subString = subString + char
                    end = end + 1
                else:
                    if len(subString) > maxLength:
                        maxLength = len(subString)
                    subString = ""
                    count = {}

            if len(subString) > maxLength:
                maxLength = len(subString)
            
            subString = ""
            i = i + 1
'''


class Solution:

    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        maxLength = 0

        while i < len(s):
            count = {}
            j = i

            while j < len(s) and s[j] not in count:
                maxLength = max(maxLength, j-i+1)
                count[s[j]] = 1
                j = j + 1

            i = i + 1

        return maxLength
 

if __name__ == "__main__":
    s = Solution()
    # print(s.lengthOfLongestSubstring("abcabcbb"))
    # print(s.lengthOfLongestSubstring("bbbbb"))
    # print(s.lengthOfLongestSubstring("pwwkew"))
    # print(s.lengthOfLongestSubstring(" "))
    print(s.lengthOfLongestSubstring("dvdf"))
