import numpy as np

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        cnt = 0
        if k == len(num):
            return '0'
        for i in num:
            if cnt > k:
                stack.append(i)
            else:
                if stack and i < stack[-1]:
                    while stack and cnt < k and i <= stack[-1]:
                        stack.pop()
                        cnt += 1
                    stack.append(i)
                else:
                    stack.append(i)
        return str(int(''.join(stack)))






if __name__ == '__main__':
    print(Solution().removeKdigits(num = "9", k = 1))