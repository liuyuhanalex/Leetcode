
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        cnt = 0
        stack = []
        for i in s:
            if i == ')':
                if stack:
                    stack.pop()
                else:
                    cnt += 1
            else:
                stack.append('(')
        return cnt


if __name__ == '__main__':
    Solution().minAddToMakeValid("())")