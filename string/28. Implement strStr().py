

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        window_size = len(needle)
        for i in range(len(haystack) - window_size):
            if haystack[i:i+window_size] == needle:
                return i
        return -1


if __name__ == '__main__':
    print(Solution().strStr(haystack="hello", needle="ll"))