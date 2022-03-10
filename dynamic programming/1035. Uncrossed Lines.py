from typing import List

class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        dp = [[0 for _ in range(len(nums1)+1)] for _ in range(len(nums2)+1)]
        for i in range(len(nums2)):
            for j in range(len(nums1)):
                if nums1[j] == nums2[i]:
                    dp[i+1][j+1] = dp[i][j] + 1
                else:
                    dp[i+1][j+1] = max(dp[i][j+1], dp[i+1][j])
        return dp[-1][-1]





if __name__ == '__main__':
    print(Solution().maxUncrossedLines(nums1 = [2,5,1,2,5], nums2 = [10,5,2,1,5,2]))