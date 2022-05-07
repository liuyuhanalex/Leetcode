class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        last_char = s[0]
        for i in s:
            if i == last_char:
                stack.append(i)
            else:
                while len(stack) >= k and len(set(stack[-k:])) == 1:
                    for _ in range(k):
                        stack.pop()
                stack.append(i)
            last_char = stack[-1]
        if len(stack) >= k and len(set(stack[-k:])) == 1:
            for _ in range(k):
                stack.pop()
        return ''.join(stack)



if __name__ == '__main__':
    #Solution().removeDuplicates(s = "deeedbbcccbdaa", k = 3)
    #print(Solution().removeDuplicates("yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", 4))
    print(Solution().removeDuplicates("wilddddddddddgooowwwwwwwwwwoooossssssssssoccccccchhhhhhhhhhcccccccccccccooryyyyyyyffffffffffyyynaicv", 10))