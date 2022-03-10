class Solution:
    def removeDuplicates(self, s: str) -> str:
        queue = [0]
        for i in s:
            if i == queue[-1]:
                queue = queue[:-1]
            else:
                queue.append(i)
        return ''.join(queue[1:])


if __name__ == '__main__':
    print(Solution().removeDuplicates(s ="abbaca"))