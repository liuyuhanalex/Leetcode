from typing import List


class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        pos = -1
        if ruleKey == 'type':
            pos = 0
        elif ruleKey == 'color':
            pos = 1
        else:
            pos = 2
        res = []
        for i in items:
            if i[pos] == ruleValue:
                res.append(i)
        return res



if __name__ == '__main__':
    Solution().countMatches()