from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dict_res = {}
        for index, i in enumerate(numbers):
            if dict_res.get(i) is not None:
                return [dict_res.get(i), index+1]
            else:
                dict_res[target-i] = index+1
        return []


if __name__ == '__main__':
    print(Solution().twoSum(numbers=[2, 7, 11, 15], target=9))