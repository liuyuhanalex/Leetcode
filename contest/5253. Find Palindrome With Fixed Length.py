from typing import List
from math import ceil

class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        max_num = ceil(intLength/2)
        max_num = 10 ** (max_num -1) * 9
        res = []
        for i in queries:
            if i > max_num:
                res.append(-1)
            res_ans = []
            while i >= 1:
                remain = i % 10
                res_ans.append(remain)
                i /= 10
            s = ''
            for j in res_ans:
                s += str(j-1)


if __name__ == '__main__':
    Solution().kthPalindrome(queries = [2,4,6], intLength = 4)
