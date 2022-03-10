class Solution:
    def trailingZeroes(self, n: int) -> int:
        total_num = 0
        while n >= 5:
            total_num += n//5
            n = n//5
        return total_num


if __name__ == '__main__':
    print(Solution().trailingZeroes(200))
