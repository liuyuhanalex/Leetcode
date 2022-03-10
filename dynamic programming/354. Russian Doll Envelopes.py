from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        sorted_envelopes = sorted(envelopes, key=lambda x: [x[0], - x[1]])
        dp = [1] * len(envelopes)
        max_num = 1
        for i in range(len(sorted_envelopes)):
            for j in range(0, i):
                if sorted_envelopes[j][1] < sorted_envelopes[i][1]:
                    dp[i] = max(dp[i], dp[j] + 1)
            if dp[i] > max_num:
                max_num = dp[i]
        return max_num




if __name__ == '__main__':
    print(Solution().maxEnvelopes(envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]))
    print(Solution().maxEnvelopes([[5,4],[6,4],[6,7],[2,3]]))