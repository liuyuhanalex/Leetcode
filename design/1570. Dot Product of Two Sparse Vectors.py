from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.store_list = {}
        for index, i in enumerate(nums):
            if i != 0:
                self.store_list[index] = i


    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        total = 0
        for i in self.store_list.keys():
            if vec.store_list.get(i) is not None:
                total += i * vec.store_list.get(i)
        return total
