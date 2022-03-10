from typing import List
from copy import copy


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        queue = ['0000']
        hash_set = set(deadends)
        visited = set('0000')
        level = 0
        while queue:
            q_len = len(queue)
            for _ in range(q_len):
                num = queue.pop(0)
                if num == target:
                    return level
                for i in range(4):
                    plus_one_num = self.plus_one(num, i)
                    if plus_one_num not in visited and plus_one_num not in hash_set:
                        queue.append(plus_one_num)
                        visited.add(plus_one_num)
                    sub_one_num = self.sub_one(num, i)
                    if sub_one_num not in visited and sub_one_num not in hash_set:
                        queue.append(sub_one_num)
                        visited.add(sub_one_num)
            level += 1
        return -1

    def plus_one(self, num, i):
        if num[i] == '9':
            return num[:i] + '0' + num[i+1:]
        else:
            return num[:i] + str(int(num[i])+1) + num[i+1:]

    def sub_one(self, num ,i):
        if num[i] == '0':
            return num[:i] + '9' + num[i+1:]
        else:
            return num[:i] + str(int(num[i])-1) + num[i+1:]


if __name__ == '__main__':
    print(Solution().openLock(["0201","0101","0102","1212","2002"], "0202"))