
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        para_dict = {"[": "]", "(": ")", "{": "}"}
        for i in s:
            if len(stack) > 0 and para_dict.get(stack[-1]) == i:
                stack.pop()
            else:
                stack.append(i)
        if len(stack) > 0:
            return False
        else:
            return True


if __name__ == '__main__':
    Solution().isValid('()[]{}')