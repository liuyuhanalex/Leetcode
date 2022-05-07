from typing import List


class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 != 0:
            return []
        else:
            mid = num // 3
            return [mid - 1, mid, mid + 1]


if __name__ == '__main__':
    print(Solution().sumOfThree(num = 33))