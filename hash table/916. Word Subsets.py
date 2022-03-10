from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        hash_table = {}
        for i in words2:
            counter = Counter(i)
            for k, v in counter.items():
                if hash_table.get(k, 0) < v:
                    hash_table[k] = v
        res = []
        for w in words1:
            w_c = Counter(w)
            if len([k for k, v in hash_table.items() if w_c.get(k, 0) >= v]) == len(hash_table):
                res.append(w)
        return res




if __name__ == '__main__':
    Solution().wordSubsets(words1 = ["amazon","apple","facebook","google","leetcode"], words2 = ["ec","oc","ceo"])