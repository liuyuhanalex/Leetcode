from typing import List
from math import ceil


class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        final_res = []
        ceil_num = ceil(intLength / 2)
        max_num = 10 ** (ceil_num - 1) * 9
        base_num = 10 ** ceil_num + 1
        for i in queries:
            if i > max_num:
                final_res.append(-1)
                continue
            res = []
            num = i
            while num > 1:
                if num % 10 - 1 < 0:
                    res.append(9)
                    num -= 1
                else:
                    res.append(num % 10 - 1)
                num = num/10
            cnt = 0
            s = ''
            while cnt < ceil_num:
                cnt += 1
                if len(res) > 0:
                    num = int(res.pop(0))
                else:
                    num = 0
                s += str(num)
            if intLength % 2 == 0:
                final_res.append(int(s[::-1] + s) + base_num)
            else:
                final_res.append(int(s[::-1][:-1] + s) + base_num)
        return final_res


if __name__ == '__main__':
    #print(Solution().kthPalindrome(queries = [1,2,3,4,5,90], intLength = 3))
    print(Solution().kthPalindrome([13], 3))