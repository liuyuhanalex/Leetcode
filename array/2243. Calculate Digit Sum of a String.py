class Solution:
    def digitSum(self, s: str, k: int) -> str:
        while len(s) > k:
            new_s = ''
            for i in range(0, len(s), k):
                num_list = list(s[i:i+k])
                total = sum([int(i) for i in num_list])
                new_s += str(total)
            s = new_s
        return s


if __name__ == '__main__':
    print(Solution().digitSum(s = "11111222223", k = 3))