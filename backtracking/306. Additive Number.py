from copy import copy
class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        result = []
        path = []
        def backtracking(index):
            if len(result) > 0:
                return
            if index == len(num) and len(path) >= 3:
                result.append(copy(path))
                return
            for i in range(index+1, len(num)+1):
                if len(path) >= 2:
                    if int(num[index: i]) == path[-1] + path[-2] and len(num[index:i]) == len(str(int(num[index:i]))):
                        path.append(int(num[index: i]))
                        backtracking(i)
                        path.pop()
                else:
                    if len(num[index:i]) == len(str(int(num[index:i]))):
                        path.append(int(num[index: i]))
                        backtracking(i)
                        path.pop()
        backtracking(0)
        if len(result) > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    print(Solution().isAdditiveNumber("1023"))