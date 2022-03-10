
class Solution:
    def isValid(self, s: str) -> bool:
        sign_dict = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        stack = []
        for i in s:
            if i in {'(', '[', '{'}:
                stack.append(i)
            else:
                if len(stack)>0 and sign_dict.get(i) == stack[-1]:
                    stack.pop(-1)
                else:
                    return False
        if len(stack) == 0:
            return True
        return False





if __name__ == '__main__':
    print(Solution().isValid("()[]{}"))
    print(Solution().isValid("([)]"))
