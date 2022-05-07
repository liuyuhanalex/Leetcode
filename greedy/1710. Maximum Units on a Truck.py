from typing import List


class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        sorted_boxes = sorted(boxTypes, key=lambda x: x[1], reverse=True)
        cnt = 0
        for i in sorted_boxes:
            box_num = min(truckSize, i[0])
            truckSize -= box_num
            cnt += box_num * i[1]
            if truckSize == 0:
                return cnt
        return cnt


if __name__ == '__main__':
    print(Solution().maximumUnits(boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10))