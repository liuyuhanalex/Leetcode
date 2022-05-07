
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        hash_table = {}
        for i in s:
            hash_table[i] = hash_table.get(i, 0) + 1
        stack = []
        for i in s:
            hash_table[i] = hash_table[i] - 1
            if i not in stack:
                while stack and i < stack[-1] and hash_table.get(stack[-1]) > 0:
                    stack.pop()
                stack.append(i)
        return ''.join(stack)


if __name__ == '__main__':
    #Solution().smallestSubsequence(s = "cbacdcbc")
    print(Solution().smallestSubsequence('bcabc'))