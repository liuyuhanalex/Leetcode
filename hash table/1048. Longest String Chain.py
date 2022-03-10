from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        hash_table = {}
        for i in words:
            hash_table.setdefault(len(i), []).append(i)
        cnt_hash_table = {}
        for i in words:
            cnt_hash_table[i] = 1
        for length in sorted(hash_table.keys(), reverse=True):
            word_list = hash_table.get(length)
            for word in word_list:
                for i in range(len(word)):
                    new_word = word[:i] + word[i+1:]
                    if new_word in hash_table.get(length-1, []):
                        cnt_hash_table[new_word] = max(cnt_hash_table.get(new_word, 0), cnt_hash_table.get(word) + 1)
        return max(cnt_hash_table.values())


if __name__ == '__main__':
    Solution().longestStrChain(words=["a","ab","ac","bd","abc","abd","abdd"])