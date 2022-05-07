

class Solution:
    def waysToBuyPensPencils(self, total: int, cost1: int, cost2: int) -> int:
        n = 0
        cnt = 0
        while n*cost1 <= total:
            remain = total - n * cost1
            cnt += remain//cost2 + 1
            n += 1
        return max(cnt, 1)


if __name__ == '__main__':
    print(Solution().waysToBuyPensPencils(total = 20, cost1 = 10, cost2 = 5))
    print(Solution().waysToBuyPensPencils(total = 5, cost1 = 10, cost2 = 10))
    print(Solution().waysToBuyPensPencils(100, 1, 1))