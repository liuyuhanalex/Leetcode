from typing import List

class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        final_set = set()
        for i in circles:
            i_range_x = [i[0] - i[2], i[0] + i[2]]
            i_range_y = [i[1] - i[2], i[1] + i[2]]
            for x in range(i_range_x[0], i_range_x[1]+1, 1):
                for y in range(i_range_y[0], i_range_y[1]+1, 1):
                    if (x-i[0])**2 + (y-i[1]) ** 2 <= i[2] ** 2:
                        print(x, y)
                        final_set.add((x, y))
        return len(final_set)


if __name__ == '__main__':
    print(Solution().countLatticePoints(circles = [[2,2,2],[3,4,1]]))