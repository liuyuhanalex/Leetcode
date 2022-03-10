from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start, end = 0, len(matrix)-1
        while end - start > 1:
            pivot = start + (end-start)//2
            if target < matrix[pivot][0]:
                end = pivot
            else:
                start = pivot
        search_list = matrix[start] + matrix[end]
        if target in set(search_list):
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().searchMatrix(matrix=[[1, 3, 5, 7],
                                          [10, 11, 16, 20],
                                          [23, 30, 34, 60]], target=3))
