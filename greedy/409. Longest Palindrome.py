class Solution:
    def longestPalindrome(self, s: str) -> int:
        hash_table = {}
        for i in s:
            hash_table[i] = hash_table.get(i, 0) + 1
        cnt = 0
        for k, v in hash_table.items():
            if v % 2 == 0:
                cnt += v
            else:
                cnt += v - 1
        if cnt < len(s):
            cnt += 1
        return cnt





if __name__ == '__main__':
    print(Solution().longestPalindrome("abccccdd"))