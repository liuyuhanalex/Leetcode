import numpy as np


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        res = {1}
        L1, L2, L3 = [2], [3], [5]
        while len(res) < n:
            min_num = min([L1[0], L2[0], L3[0]])
            if L1[0] == min_num:
                L1.pop(0)
            if L2[0] == min_num:
                L2.pop(0)
            if L3[0] == min_num:
                L3.pop(0)
            L1.append(min_num*2)
            L2.append(min_num*3)
            L3.append(min_num*5)
            res.add(min_num)
        return max(res)





if __name__ == '__main__':
    print(Solution().nthUglyNumber(400))