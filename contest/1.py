from typing import List

class Solution:
    def divideString(self, s: str, k: int, fill: str) -> List[str]:
        s_list = list(s)
        cnt = 0
        res_str = ''
        res = []
        while s_list:
            res_str += s_list.pop(0)
            cnt += 1
            if cnt % k == 0:
                res.append(res_str)
                res_str = ''
        if len(res_str) < k:
            res_str += fill*(k-len(res_str))
            res.append(res_str)
        return res





if __name__ == '__main__':
    Solution().divideString(s = "abcdefghij", k = 3, fill = "x")