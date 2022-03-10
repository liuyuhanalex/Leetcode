from math import sqrt

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num == 1:
            return False
        res = 1
        for i in range(2, int(sqrt(num)) + 1):
            if num % i == 0:
                res += i + num//i
        return res == num


if __name__ == '__main__':
    print(Solution().checkPerfectNumber(28))