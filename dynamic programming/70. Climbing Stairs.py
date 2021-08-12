class Solution:
    def climbStairs(self, n: int) -> int:
        result_list = [1, 2] + [0]*(n-2)
        for i in range(2, n):
            result_list[i] = result_list[i-1] + result_list[i-2]
        return result_list[n-1]