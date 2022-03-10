from typing import List


class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        # dp数组记录的是已这个数字结尾，difference为相应数值的数组max length
        dp = [1 for _ in range(len(arr))]
        hash_table = {}
        for i in range(len(arr)):
            if hash_table.get(arr[i]-difference) is not None:
                dp[i] = hash_table.get(arr[i] - difference) + 1
                hash_table[arr[i]]  = dp[i]
            else:
                hash_table[arr[i]] = 1
        return max(dp)



if __name__ == '__main__':
    print(Solution().longestSubsequence(arr = [1,5,7,8,5,3,4,2,1], difference = -2))