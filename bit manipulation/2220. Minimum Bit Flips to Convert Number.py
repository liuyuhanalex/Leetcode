
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        res = 0
        for i in range(32):
            if (start & (1 << i)) != (goal & (1 << i)):  # count if i-th bit is diff for a and b
                res += 1
        return res



if __name__ == '__main__':
    Solution().minBitFlips( start = 10, goal = 7)