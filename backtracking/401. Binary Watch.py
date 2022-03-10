from typing import List
from copy import copy

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 回溯方法
        if turnedOn > 8:
            return []
        res = set()
        path = []
        choice_list = {100, 200, 400, 800, 1, 2, 4, 8, 16, 32}
        def backtracking(choice_set):
            if len(path) == turnedOn:
                sum_num = sum(path)
                h_num = sum_num//100
                m_num = sum_num % 100
                if h_num < 12 and m_num < 60:
                    res_str = str(h_num) + ':'
                    if len(str(m_num)) < 2:
                        res_str += '0' + str(m_num)
                    else:
                        res_str += str(m_num)
                    res.add(res_str)
                return
            for i in choice_set:
                path.append(i)
                backtracking(choice_set - {i})
                path.pop()
        backtracking(choice_list)
        return res

if __name__ == '__main__':
    print(Solution().readBinaryWatch(2))