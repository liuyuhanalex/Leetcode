from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        queue = []
        res = tokens[0]
        while tokens:
            sign = tokens.pop(0)
            if sign == '+':
                res = queue.pop() + queue.pop()
                tokens = [res] + tokens
            elif sign == '-':
                num1 = queue.pop()
                num2 = queue.pop()
                res = num2 - num1
                tokens = [res] + tokens
            elif sign == '*':
                res = queue.pop() * queue.pop()
                tokens = [res] + tokens
            elif sign == '/':
                num1 = queue.pop()
                num2 = queue.pop()
                res = int(num2/num1)
                tokens = [res] + tokens
            else:
                queue.append(int(sign))
        return res


if __name__ == '__main__':
    print(Solution().evalRPN(tokens = ["4","13","5","/","+"]))
    Solution().evalRPN(["2","1","+","3","*"])
    print(Solution().evalRPN(["4","3","-"]))
