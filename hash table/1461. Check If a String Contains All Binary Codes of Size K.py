class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        res_set = set()
        for i in range(len(s) - k + 1):
            res_set.add(s[i: i+k])
        if len(res_set) != 2**k:
            return False
        return True



if __name__ == '__main__':
    print(Solution().hasAllCodes(s = "00110", k = 2))