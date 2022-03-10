from typing import List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        x_hash_table = {}
        for i in points:
            x_hash_table.setdefault(i[0], set()).add(i[1])
        x_list = sorted(x_hash_table.keys())
        area = []
        for i in range(len(x_list)):
            i_set = x_hash_table.get(x_list[i])
            for j in range(i+1, len(x_list)):
                j_set = x_hash_table.get(x_list[j])
                intersect = i_set.intersection(j_set)
                wid = x_list[j] - x_list[i]
                if len(intersect) >= 2:
                    for z in sorted(intersect):
                        if z+wid in intersect:
                            area.append(wid*wid)
                            break
        return min(area)







if __name__ == '__main__':
    print(Solution().minAreaRect([[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]))