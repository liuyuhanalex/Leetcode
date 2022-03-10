from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = []
        for i in range(numRows):
            line_list = [1] * (i+1)
            for j in range(1, i):
                line_list[j] = res[i-1][j] + res[i-1][j-1]
            res.append(line_list)
        return res





if __name__ == '__main__':
    Solution().generate(numRows=5)
