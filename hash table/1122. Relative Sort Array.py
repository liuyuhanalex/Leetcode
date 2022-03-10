from typing import List


class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        hash_table = {}
        for num in arr1:
            hash_table[num] = hash_table.get(num, 0) + 1
        res = []
        for i in arr2:
            if hash_table.get(i) is not None:
                res += [i]*hash_table.get(i)
                hash_table[i] = 0
        append_list = sorted([i for i in arr1 if i not in arr2])
        return res + append_list





if __name__ == '__main__':
    print(Solution().relativeSortArray(arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]))