from typing import List

class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        # 位运算
        total_set = set()
        for i in startWords:
            w_b = 0
            for w in i:
                w_b |= 1 << ord(w) - ord('a')
            total_set.add(w_b)
        cnt = 0
        for j in targetWords:
            w_b = 0
            for i in j:
                w_b |= 1 << ord(i) - ord('a')
            for pos_w in j:
                if w_b ^ (1<<(ord(pos_w) - ord('a'))) in total_set:
                    cnt += 1
                    break
        return cnt


if __name__ == '__main__':
    print(Solution().wordCount(startWords = ["ant","act","tack"], targetWords = ["tack","act","acti"]))