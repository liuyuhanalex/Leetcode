from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res_dict = {}
        for str in strs:
            res_str = ' '.join(sorted(str))
            res_dict.setdefault(res_str, []).append(str)
        return list(res_dict.values())


if __name__ == '__main__':
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
