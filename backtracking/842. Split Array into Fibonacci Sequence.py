from typing import List
from copy import copy


class Solution:
    def splitIntoFibonacci(self, num: str) -> List[int]:
        result = []
        path = []
        def backtracking(index):
            if len(result) > 0:
                return
            if index == len(num) and len(path) >= 3:
                result.append(copy(path))
                return
            for i in range(len(num[index: index+10+1])):
                new_num = num[index: index+i+1]
                if len(new_num) == len(str(int(new_num))) and int(new_num) <= 2147483647:
                    if len(path) >= 2:
                        if int(new_num) == path[-1] + path[-2]:
                            path.append(int(new_num))
                            backtracking(index+i+1)
                            path.pop()
                    else:
                        path.append(int(new_num))
                        backtracking(index+i+1)
                        path.pop()
        backtracking(0)
        return result[0] if len(result) > 0 else []


if __name__ == '__main__':
    print(Solution().splitIntoFibonacci(num="539834657215398346785398346991079669377161950407626991734534318677529701785098211336528511"))