from typing import List
from collections import Counter


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)
        cnt = 0
        for k, v in counter.items():
            remain = v % 3
            num = v // 3
            if remain == 0 or (remain==1 and num > 1) or remain ==2:
                if remain == 0:
                    cnt += num
                elif remain == 1:
                    cnt += num - 1 + 2
                else:
                    cnt += num + 1
            else:
                return -1
        return cnt


if __name__ == '__main__':
    print(Solution().minimumRounds(tasks = [2,2,3,3,2,4,4,4,4,4]))