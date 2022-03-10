from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        sorted_citations = sorted(citations)
        total = len(sorted_citations)
        h_index = 0
        for i in range(len(sorted_citations)):
            remain = total - i
            if sorted_citations[i] >= remain:
                h_index = remain
                break
        return h_index



if __name__ == '__main__':
    Solution().hIndex(citations = [3,0,6,1,5])