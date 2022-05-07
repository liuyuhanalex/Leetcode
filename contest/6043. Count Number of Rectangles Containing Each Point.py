from typing import List
import bisect


class Solution:
    def countRectangles(self, rectangles: List[List[int]], points: List[List[int]]) -> List[int]:
        hash_table = {}
        rectangles = sorted(rectangles, key=lambda x: [x[0], x[1]])
        for i in rectangles:
            hash_table.setdefault(i[0], []).append(i[1])
        keys = list(hash_table.keys())
        final = []
        for i in points:
            if i[0] <= keys[-1]:
                pos = bisect.bisect_left(keys, i[0])
                cnt = 0
                for j in keys[pos:]:
                    r_l = hash_table.get(j)
                    pos2 = bisect.bisect_left(r_l, i[1])
                    cnt += len(r_l) - pos2
                final.append(cnt)
            else:
                final.append(0)
        return final




if __name__ == '__main__':
    print(Solution().countRectangles(rectangles = [[1,1],[2,2],[3,3]], points = [[1,3],[1,1]]))