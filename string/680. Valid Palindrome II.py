class Solution:
    def validPalindrome(self, s: str) -> bool:
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                s_new = s[:start] + s[start+1:]
                if s_new == s_new[::-1]:
                    return True
                s_new_2 = s[:end] + s[end+1:]
                if s_new_2 == s_new_2[::-1]:
                    return True
                print(s_new_2, s_new)
                return False
            start += 1
            end -= 1
        return False



if __name__ == '__main__':
    print(Solution().validPalindrome("abca"))