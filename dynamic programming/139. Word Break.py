from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [0] * (len(s)+1)
        dp[0] = 1
        word_set = set(wordDict)
        length = list({len(i) for i in wordDict})
        for index in range(len(s)+1):
            if index >= min(length):
                for j in length:
                    if s[index-j: index] in word_set and dp[index-j] == 1 and index<=len(s):
                        dp[index] = 1
                        break
        return dp[-1]





if __name__ == '__main__':
    Solution().wordBreak(s="leetcode",
                         wordDict=["leet", "code"])