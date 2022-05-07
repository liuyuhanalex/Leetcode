class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        last = s[0]
        cnt = 1
        res = []
        for i in s[1:]:
            if i == last:
                cnt += 1
            else:
                last = i
                res.append(cnt)
                cnt = 1
        res.append(cnt)
        cnt = 0
        for index in range(len(res) -1):
            cnt += max(res[index], res[index+1])
        return cnt


if __name__ == '__main__':
    print(Solution().countBinarySubstrings(s = "00110011"))