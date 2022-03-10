class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        start, end = 0, min(len(s)-1, k-1)
        res = ''
        while True:
            res += s[start: end+1][::-1]
            if end == len(s) - 1:
                break
            if start + 2*k <= len(s) - 1:
                res += s[end+1:end + k +1]
                start = start+2*k
            else:
                start = end + 1
            end = min(start + k - 1, len(s)-1)
        return res


if __name__ == '__main__':
    print(Solution().reverseStr(s = "abcdefg", k = 2))