from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        first_row = "qwertyuiop"
        second_row = "asdfghjkl"
        third_row = "zxcvbnm"
        hash_table = {}
        for i in first_row:
            hash_table[i] = 1
            hash_table[i.upper()] = 1
        for i in second_row:
            hash_table[i] = 2
            hash_table[i.upper()] = 2
        for i in third_row:
            hash_table[i] = 3
            hash_table[i.upper()] = 3
        final_res = []
        for i in words:
            res = []
            for j in i:
                res.append(hash_table.get(j))
            if len(set(res)) == 1:
                final_res.append(i)
        return final_res






if __name__ == '__main__':
    Solution().findWords(words = ["Hello","Alaska","Dad","Peace"])