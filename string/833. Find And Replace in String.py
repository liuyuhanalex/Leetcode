from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        string_list = list(s)
        mark_list = [True] * len(s)
        for index, i in enumerate(indices):
            replace_str = sources[index]
            if ''.join(string_list[i:i+len(replace_str)]) == replace_str and all(mark_list[i: i+len(replace_str)]) is True:
                string_list[i] = targets[index]
                mark_list[i] = False
                for j in range(i+1, i+len(replace_str)):
                    string_list[j] = ''
                    mark_list[j] = False
        return ''.join(string_list)


if __name__ == '__main__':
    print(Solution().findReplaceString(s = "abcd", indices = [0, 2], sources = ["ab","ec"], targets = ["eee", "ffff"]))