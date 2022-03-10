from typing import List


class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        dif_candy = set(candyType)
        if len(dif_candy) < len(candyType) // 2:
            return len(dif_candy)
        else:
            return len(candyType)//2


if __name__ == '__main__':
    print(Solution().distributeCandies([1, 1, 2, 2, 3, 3]))