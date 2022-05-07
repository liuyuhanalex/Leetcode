

class Solution:
    def countOperations(self, num1: int, num2: int) -> int:
        cnt = 0
        while num1 != 0 and num2 !=0:
            if num1 > num2:
                num1 -= num2
            else:
                num2 -= num1
            cnt += 1
        return cnt


if __name__ == '__main__':
    print(Solution().countOperations(num1 = 2, num2 = 3))