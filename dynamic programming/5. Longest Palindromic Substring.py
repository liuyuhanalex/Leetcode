import numpy as np
class Solution:
    # brute force solution
    def longestPalindrome_brute_force(self, s: str) -> str:
        if len(s) == 1:
            return s
        s_array = list(s)
        max_num = 0
        result = ""
        for i in range(len(s), len(s) - max_num):
            for j in range(i + max_num, len(s)+1):
                ori_array = s_array[i:j]
                reversed_array = ori_array[::-1]
                if ori_array == reversed_array and j-i+1 >= max_num:
                    result = "".join(ori_array)
                    max_num = j-i+1
        return result

    # dynamic programming solution
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1 or list(s) == list(reversed(list(s))):
            return s
        dp = np.zeros((len(s), len(s)))
        for i in range(len(s)):
            dp[i][i] = 1
        max_i, max_j = 0, 0
        for i in reversed(range(len(s))):
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1]
                    if j == i+1:
                        dp[i][j] = 1
                if dp[i][j]:
                    if j - i + 1 > max_j - max_i + 1:
                        max_i, max_j = i, j
        return s[max_i: max_j+1]


if __name__ == '__main__':
    Solution().longestPalindrome("cbbd")
