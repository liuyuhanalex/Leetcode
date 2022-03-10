from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        hash_table = {}
        for i in matrix:
            sign = ''.join([str(j) for j in i])
            reverse_sign = ''.join([str(1-j) for j in i])
            if hash_table.get(sign) is not None:
                hash_table[sign] = hash_table[sign] + 1
            else:
                if hash_table.get(reverse_sign) is not None:
                    hash_table[reverse_sign] = hash_table[reverse_sign] + 1
                else:
                    hash_table[sign] = 1
        max_num = sorted(hash_table.values(), reverse=True)[0]
        return max_num



if __name__ == '__main__':
    Solution().maxEqualRowsAfterFlips([[0,0,0],[0,0,1],[1,1,0]])