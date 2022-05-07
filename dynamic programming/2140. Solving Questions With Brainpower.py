from typing import List


class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        dp = [0 for _ in range(200001)]
        dp[len(questions) - 1] = questions[-1][0]
        for i in range(len(questions) - 2, -1, -1):
            dp[i] = max(dp[i+1], dp[i + 1 + questions[i][1]] + questions[i][0])
        return max(dp)


if __name__ == '__main__':
    Solution().mostPoints(questions = [[1,1],[2,2],[3,3],[4,4],[5,5]])