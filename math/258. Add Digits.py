

class Solution:
    def addDigits(self, num: int) -> int:
        total = 0
        while num > 0:
            total += num % 10
            num = num //10
        return total % 9 if total > 9 else total



if __name__ == '__main__':
    Solution().addDigits(384)