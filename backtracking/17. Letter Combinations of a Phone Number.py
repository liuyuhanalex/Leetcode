from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        num_letter_dict = {
            '2': ['a', 'b', 'c'],
            '3': ['d', 'e', 'f'],
            '4': ['g', 'h', 'i'],
            '5': ['j', 'k', 'l'],
            '6': ['m', 'n', 'o'],
            '7': ['p', 'q', 'r', 's'],
            '8': ['t', 'u', 'v'],
            '9': ['w', 'x', 'y', 'z']
        }
        if len(digits) == 0:
            return []
        char_list = [num_letter_dict.get(char) for char in digits]
        path = []
        result = []
        def backtracking(char_list, start_index):
            if len(path) == len(char_list):
                result.append(''.join(path))
                return
            for i in char_list[start_index]:
                path.append(i)
                backtracking(char_list, start_index + 1)
                path.pop()
        backtracking(char_list, 0)
        return result