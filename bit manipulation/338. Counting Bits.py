from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        res = []
        for i in range(n+1):
            sum_list = []
            while i > 0:
                sum_list.append(i & 1)
                i >>= 1
            res.append(sum(sum_list))
        return res


if __name__ == '__main__':
    Solution().countBits(n = 5)

