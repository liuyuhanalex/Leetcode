class Solution:
    def reverseVowels(self, s: str) -> str:
        pointer1, pointer2 = 0, len(s) - 1
        s = list(s)
        while pointer1 < pointer2:
            if s[pointer1] not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                pointer1 += 1
                continue
            if s[pointer2] not in {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}:
                pointer2 -= 1
                continue
            s[pointer1] , s[pointer2] = s[pointer2], s[pointer1]
            pointer1 += 1
            pointer2 -= 1
        return ''.join(s)

if __name__ == '__main__':
    Solution().reverseVowels( s = "ai")