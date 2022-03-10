from typing import List
import copy


class Solution:
    def letterCasePermutation_test(self, s: str) -> List[str]:
        result = []
        s_list = [i for i in s if ord('A') <= ord(i) <=ord('z')]
        print(s_list)
        def backtracking(pre_list, path):
            if len(path) == len(s_list):
                result.append(copy.copy(path))
            for index, i in enumerate(pre_list):
                for j in list({i, i.upper(), i.lower()}):
                    path.append(j)
                    backtracking(pre_list[index+1:], path)
                    path.pop()
        backtracking(s_list, [])
        print(result)

    def letterCasePermutation(self, s: str) -> List[str]:
        result = []
        def backtracking(char_list, path):
            len_p = len(path)
            if len_p == len(s):
                result.append(path)
            for index, i in enumerate(char_list):
                if ord('A') <= ord(i) <=ord('z'):
                    for j in list({i, i.upper(), i.lower()}):
                        path += j
                        backtracking(char_list[index+1:], path)
                        path = path[:len_p]
                else:
                    path += i
                    backtracking(char_list[index+1:], path)
                    path = path[:len_p]
        backtracking(list(s), '')
        return result


if __name__ == '__main__':
    print(Solution().letterCasePermutation(s="a1b2"))
