class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 3:
            return True
        if n % 3 != 0:
            return False
        return self.isPowerOfThree(n//3)


if __name__ == '__main__':
    print(Solution().isPowerOfThree(27))