from typing import List

class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        dp_before = [0 for _ in range(len(security))]
        dp_after = [0 for _ in range(len(security))]
        for i in range(1, len(security)):
            if security[i] <= security[i-1]:
                dp_before[i] = dp_before[i-1] + 1
            else:
                dp_before[i] = 0
        for i in range(len(security)-2, -1, -1):
            if security[i] <= security[i+1]:
                dp_after[i] = dp_after[i+1] + 1
            else:
                dp_after[i] = 0
        index = 0
        final_result = []
        for i, j in zip(dp_before, dp_after):
            if i >= time and j >= time:
                final_result.append(index)
            index += 1
        return final_result






if __name__ == '__main__':
    #print(Solution().goodDaysToRobBank(security = [5,3,3,3,5,6,2], time = 2))
    print(Solution().goodDaysToRobBank([1, 2, 3, 4], 1))