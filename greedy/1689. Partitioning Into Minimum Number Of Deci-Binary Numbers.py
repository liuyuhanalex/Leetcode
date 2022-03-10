

class Solution:
    def minPartitions(self, n: str) -> int:
        n_list = list(n)
        return int(max(n_list))


if __name__ == '__main__':
    Solution().minPartitions(n = "82734")