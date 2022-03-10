from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        res = []
        for index, i in enumerate(points):
            dis = i[0] * i[0] + i[1]* i[1]
            res.append((dis, i))
        sorted_res = sorted(res, key=lambda x: x[0])
        final_res = [i[1] for i in sorted_res[:k]]
        return final_res




if __name__ == '__main__':
    print(Solution().kClosest(points = [[-5,4],[-6,-5],[4,6]], k = 2))