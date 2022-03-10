class Solution:
    def firstUniqChar(self, s: str) -> int:
        res_dict = {}
        for i in s:
            res_dict[i] = res_dict.get(i, 0) + 1
        res_set = set()
        for k, v in res_dict.items():
            if v == 1:
                res_set.add(k)
        for index, i in enumerate(s):
            if i in res_set:
                return index
        return -1




if __name__ == '__main__':
    print(Solution().firstUniqChar(s="loveleetcode"))