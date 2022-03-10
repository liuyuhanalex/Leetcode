class Solution:
    def convert(self, s: str, numRows: int) -> str:
        res = ['' for _ in range(numRows)]
        total = 2 * numRows - 2
        for i in range(len(s)):
            remain = i % total
            row_num = min(remain, total - remain)
            res[row_num] += s[i]
        return ''.join(res)


if __name__ == '__main__':
    print(Solution().convert(s = "PAYPALISHIRING", numRows = 4))