from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        start, end = 0, len(citations)
        length = end
        while start < end:
            mid = start + (end - start)//2
            remain = length - mid
            if citations[mid] > remain:
                end = mid - 1
            else:
                start = mid
        return citations[start]


if __name__ == '__main__':
    print(Solution().hIndex(citations=[0, 1, 3, 5, 6]))