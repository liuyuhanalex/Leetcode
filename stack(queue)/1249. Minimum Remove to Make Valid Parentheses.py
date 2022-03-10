

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        final_stack = []
        res = []
        for index, i in enumerate(s):
            if i == '(':
                final_stack.append(index)
            elif i == ')':
                if not final_stack:
                    res.append(index)
                else:
                    final_stack.pop()
        while final_stack:
            res.append(final_stack.pop())
        s_list = list(s)
        while res:
            num = res.pop()
            s_list[num] = '.'
        final_str = ''.join(s_list)
        final_str = final_str.replace('.', '')
        return final_str


if __name__ == '__main__':
    Solution().minRemoveToMakeValid(s = "lee(t(c)o)de)")