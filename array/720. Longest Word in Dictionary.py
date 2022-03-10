from typing import List


class Solution:
    def longestWord(self, words: List[str]) -> str:
        hash_table = {}
        for i in words:
            hash_table.setdefault(len(i), []).append(i)
        max_length = max(hash_table.keys())
        last = {''}
        for i in range(1, max_length+1):
            content = hash_table.get(i)
            new_last = set()
            for j in content:
                if j[:-1] in last:
                     new_last.add(j)
            if len(new_last) == 0:
                return sorted(last)[0]
            last = new_last
        return max_length






if __name__ == '__main__':
    print(Solution().longestWord(words = ["a","banana","app","appl","ap","apply","apple"]))