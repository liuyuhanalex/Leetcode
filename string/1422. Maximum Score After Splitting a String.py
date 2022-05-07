

class Solution:
    def maxScore(self, s: str) -> int:
        s_list = [int(i) for i in list(s)]
        total_sum = sum(s_list)
        prefix_sum = 0
        max_num = 0
        for index, i in enumerate(s_list):
            prefix_sum += i
            if index >= 1 and index < len(s_list) - 1:
                max_num = max(max_num, total_sum - prefix_sum + index + 1 - prefix_sum)
        return max_num





if __name__ == '__main__':
    Solution().maxScore(s = "011101")
