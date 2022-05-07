from typing import List
import bisect


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], persons: List[int]) -> List[int]:
        prefix = 0
        followers_1 = [(i[0], 1) for i in flowers]
        followers_2 = [(i[1]+1, 2) for i in flowers]
        total_sorted = sorted(followers_1 + followers_2, key=lambda x: x[0])
        final = {}
        for i in total_sorted:
            if i[1] == 1:
                prefix += 1
            else:
                prefix -= 1
            final[i[0]] = prefix
        keys = list(final.keys())
        res = []
        for i in persons:
            pos = bisect.bisect_left(keys, i)
            if pos <= len(keys) - 1:
                if keys[pos] != i:
                    pos = pos-1
                res.append(final.get(keys[pos]))
            else:
                res.append(0)
        return res



if __name__ == '__main__':
    #print(Solution().fullBloomFlowers([[1,6],[3,7],[9,12],[4,13]], [2,3,7,11]))
    print(Solution().fullBloomFlowers([[19,37],[19,38],[19,35]], [6,7,21,1,13,37,5,37,46,43]))