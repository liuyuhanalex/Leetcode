class Solution:
    def minInsertions(self, s: str) -> int:
        cnt = 0
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '(':
                stack.append('(')
                i += 1
            else:
                if s[i: i+2] == '))':
                    if stack:
                        stack.pop()
                    else:
                        cnt += 1
                    i = i+2
                else:
                    if stack:
                        stack.pop()
                        cnt += 1
                    else:
                        cnt += 2
                    i += 1
        return len(stack) * 2 + cnt



if __name__ == '__main__':
    print(Solution().minInsertions(s = "(()))"))
