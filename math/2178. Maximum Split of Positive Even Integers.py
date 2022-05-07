from typing import List

class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        num_of_two = finalSum // 2
        cnt = 0
        final = []
        while num_of_two > 0:
            cnt += 1
            num_of_two -= cnt
            if num_of_two < 0:
                old_cnt = cnt - 1
                cnt = num_of_two + cnt + cnt - 1
                final.remove(2 * old_cnt)
            final.append(2*cnt)
        return final




if __name__ == '__main__':
    print(Solution().maximumEvenSplit(finalSum = 28))