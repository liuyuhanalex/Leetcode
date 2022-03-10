class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1 if dividend * divisor >=0 else -1
        dividend, divisor = abs(dividend), abs(divisor)
        res = (dividend//divisor)
        if flag == -1:
            return max(-2**31, flag * res)
        return min(2**31, res)


if __name__ == '__main__':
    print(Solution().divide(dividend = 7, divisor = -3))
