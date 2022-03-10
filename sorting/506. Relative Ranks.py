from typing import List


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        new_array = [(index, x) for index, x in enumerate(score)]
        sorted_array = sorted(new_array, key=lambda x: x[1], reverse=True)
        for index, i in enumerate(sorted_array):
            if index == 0:
                score[i[0]] = 'Gold Medal'
            elif index == 1:
                score[i[0]] = 'Silver Medal'
            elif index == 2:
                score[i[0]] = 'Bronze Medal'
            else:
                score[i[0]] = str(index+1)
        return score


if __name__ == '__main__':
    Solution().findRelativeRanks([10,3,8,9,4])