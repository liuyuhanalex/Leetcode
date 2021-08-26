import numpy as np


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # dp[i][j] 表示word1(1:i) 转换成 word2(1:j) 所需的最少步骤
        dp = np.zeros((len(word1) + 1, len(word2) + 1))
        for i in range(len(word2) + 1): dp[0][i] = i
        for i in range(len(word1) + 1): dp[i][0] = i
        word1, word2 = 'a'+word1, 'a'+word2
        for i in range(1, len(word1)):
            for j in range(1, len(word2)):
                #1.最后一个字母一样
                if word1[i] == word2[j]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    # 插入, 删除, 替换
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
        return int(dp[len(word1)-1][len(word2)-1])


if __name__ == '__main__':
    # sea eat 2
    # ab a 1
    # park spake
    print(Solution().minDistance(word1="horse", word2="ros"))


