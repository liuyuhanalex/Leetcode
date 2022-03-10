import sys

class Solution:
    def reverse(self, x: int) -> int:
        if x > 2**31 - 1 or x < -2**31:
            return 0
        new_number = 0
        sign = -1 if x < 0 else 1
        x = abs(x)
        while x != 0:
            remain = x % 10
            x = x//10
            new_number = new_number*10 + remain
        return sign*new_number


if __name__ == '__main__':
    print(Solution().reverse(x=-123))
