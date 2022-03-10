class Solution:
    def arrangeCoins(self, n: int) -> int:
        start, end = 1, n
        while start < end:
            mid = start + (end - start) // 2
            if (1 + mid)*mid//2 <= n:
                start = mid + 1
            else:
                end = mid
        return start - 1


if __name__ == '__main__':
    print(Solution().arrangeCoins(3))