

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        queue = []
        max_len = 0
        for i in range(len(s)):
            if s[i] not in queue:
                queue.append(s[i])
            else:
                len1 = len(queue)
                if len1 > max_len:
                    max_len = len1
                index = queue.index(s[i])
                for j in range(index+1):
                    queue.pop(0)
                queue.append(s[i])
        if len(queue) > max_len:
            max_len = len(queue)
        return max_len





if __name__ == '__main__':
    print(Solution().lengthOfLongestSubstring(s="au"))