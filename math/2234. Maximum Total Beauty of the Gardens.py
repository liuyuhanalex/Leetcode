from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def maximumBeauty(self, flowers: List[int], newFlowers: int, target: int, full: int, partial: int) -> int:
        incom = [i for i in flowers if i < target]
        com_num = len([i for i in flowers if i >= target])
        if len(incom) == 0:
            return len(flowers) * full
        else:
            s_income = [0]
            incom = sorted(incom, reverse=True)
            for i in range(len(incom)):
                diff = target - incom[i]
                if diff < newFlowers:
                    newFlowers -= diff
                    com_num += 1
                else:
                    s_income = incom[i:]
                    break
            heapify(s_income)
            while newFlowers > 0 and len(s_income) > 1:
                num = heappop(s_income)
                num += 1
                newFlowers -= 1
                heappush(s_income, num)
            if len(s_income) == 1:
                return max(com_num * full,  (com_num - 1) * full + partial * (target - 1))
            return com_num * full + partial * min(s_income)



if __name__ == '__main__':
    print(Solution().maximumBeauty(flowers = [2,4,5,3], newFlowers = 10, target = 5, full = 2, partial = 6))