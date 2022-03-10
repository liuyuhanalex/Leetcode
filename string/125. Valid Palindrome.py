import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            if s[start].lower() not in list(string.ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                start += 1
                continue
            if s[end].lower() not in list(string.ascii_lowercase) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
                end -= 1
                continue
            if s[start].lower() != s[end].lower():
                return False
            else:
                start += 1
                end -= 1
        return True


if __name__ == '__main__':
    print(Solution().isPalindrome("0P"))