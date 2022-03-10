class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for index, i in enumerate(goal):
            if i == s[0]:
                if s[-index:] + s[:-index] == goal:
                    return True
        return False






if __name__ == '__main__':
    print(Solution().rotateString("gcmbf", "fgcmb"))