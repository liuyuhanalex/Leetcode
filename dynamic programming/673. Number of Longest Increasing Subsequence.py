from typing import List


class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # dp 记录以这个数结尾的最大长度及个数
        if len(set(nums)) == 1:
            return len(nums)
        dp = [[1, 0] for _ in range(len(nums))]
        dp[0] = [1, 1]
        for i in range(1, len(nums)):
            array = [dp[j][0] for j in range(i) if nums[j] < nums[i]]
            if len(array) > 0:
                max_length = max(array)
            else:
                max_length = 0
            dp[i][0] = max_length + 1
            for j in range(i):
                if dp[j][0] == max_length and nums[j] < nums[i]:
                    dp[i][1] += dp[j][1]
            if dp[i][1] == 0:
                dp[i][1] = 1
        max_length = sorted(dp, key=lambda x: x[0], reverse=True)[0][0]
        cnt = 0
        for i in dp:
            if i[0] == max_length:
                cnt += i[1]
        return cnt


if __name__ == '__main__':
    #print(Solution().findNumberOfLIS(nums = [1,2,4,3,5,4,7,2]))
    #print(Solution().findNumberOfLIS(nums = [2,1]))
    #print(Solution().findNumberOfLIS([1,3,5,4,7]))
    print(Solution().findNumberOfLIS([1,1,1,2,2,2,3,3,3]))