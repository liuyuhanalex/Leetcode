from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        dif_list = [i-j for i, j in zip(gas, cost)]
        if sum(dif_list) < 0:
            return -1
        if len(dif_list) == 1:
            return 0
        sorted_dif = sorted([(i, index) for index, i in enumerate(dif_list)], key=lambda x: x[0], reverse=True)
        for item in sorted_dif:
            i, num = item
            if num > 0:
                new_list = dif_list[i:] + dif_list[0: i]
                prefix_sum = 0
                for j in range(len(new_list)):
                    prefix_sum += new_list[j]
                    if prefix_sum < 0:
                        break
                if j == len(new_list) - 1:
                    return i


if __name__ == '__main__':
    print(Solution().canCompleteCircuit([5,8,2,8], [6,5,6,6]))