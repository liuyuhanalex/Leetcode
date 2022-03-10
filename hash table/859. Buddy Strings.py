

class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if s == goal:
            if len(set(s)) < len(s):
                return True
            return False
        cnt = 0
        for i, j in zip(s, goal):
            if i != j:
                if cnt == 0:
                    res = (i, j)
                else:
                    if res != (j, i):
                        return False
                cnt += 1
                if cnt > 2:
                    return False
        return True





if __name__ == '__main__':
    print(Solution().buddyStrings(s = "ab", goal = "ab"))
    print(Solution().buddyStrings(s = 'ab', goal = 'ba'))