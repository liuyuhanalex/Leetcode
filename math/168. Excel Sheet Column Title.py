class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        string_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if columnNumber <= 26:
            return string_list[columnNumber-1]
        res = []
        while columnNumber > 26:
            num = columnNumber % 26
            if res and res[-1] == 0:
                res.append(num-1)
            else:
                res.append(num)
            columnNumber //= 26
        if res[-1] == 0:
            if columnNumber - 1 > 0:
                res = res + [columnNumber-1]
            else:
                res = res
        else:
            res = res + [columnNumber]
        return ''.join([string_list[i-1] for i in reversed(res)])



if __name__ == '__main__':
    print(Solution().convertToTitle(701))
    print(Solution().convertToTitle(2147483647))
    print(Solution().convertToTitle(702))