from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_length = min([len(i) for i in strs])
        prefix = ''
        for j in range(1, min_length+1):
            if len(set([i[:j] for i in strs])) == 1:
                prefix = strs[0][:j]
            else:
                break
        return prefix


if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["ab", "a"]))