from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        words_num = []
        for i in words:
            val = 0*26
            for w in i:
                val |= 1 << ord(w) - ord('a')
            words_num.append(val)
        res = []
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if words_num[i] & words_num[j] == 0:
                    res.append(len(words[i]) * len(words[j]))
        return max(res)

if __name__ == '__main__':
    print(Solution().maxProduct(["abcw","baz","foo","bar","xtfn","abcdef"]))