
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res_dict = {}
        for index, i in enumerate(s):
            res_dict.setdefault(i, []).append(index)
        final_dict = {}
        for i in t:
            final_dict.setdefault(i, []).append(res_dict.get(i))
        for i in final_dict.values():
            pass


if __name__ == '__main__':
    Solution().minWindow(s = "ADOBECODEBANC", t = "ABC")
