
class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        # dp数组表示在poured为一定数值的情况下，dp[i][j]杯中的饮料多少
        dp = [[0 for _ in range(i+1)] for i in range(query_row+1)]
        dp[0][0] = poured
        for i in range(1, query_row+1):
            for j in range(i+1):
                if j == 0:
                    dp[i][j] = max(dp[i-1][j]-1, 0)/2
                elif j == i:
                    dp[i][j] = max(dp[i-1][j-1]-1, 0) / 2
                else:
                    dp[i][j] = max(dp[i-1][j-1]-1, 0)/2 + max(dp[i-1][j] - 1, 0) / 2
        res = dp[query_row][query_glass]
        return min(res, 1)




if __name__ == '__main__':
    print(Solution().champagneTower(poured = 100000009, query_row = 33, query_glass = 17))
    print(Solution().champagneTower(poured=1, query_row=1, query_glass=1))
    print(Solution().champagneTower(poured=2, query_row=1, query_glass=1))
    print(Solution().champagneTower(poured=25, query_row=6, query_glass=1))