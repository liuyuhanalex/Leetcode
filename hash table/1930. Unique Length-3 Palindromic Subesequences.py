
class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        start_hash = {}
        end_hash = {}
        for i in range(len(s)):
            if start_hash.get(s[i]) is None:
                start_hash[s[i]] = i
                end_hash[s[i]] = i
            else:
                end_hash[s[i]] = i
        final_set = set()
        for i in start_hash.keys():
            if start_hash[i] != end_hash[i]:
                for j in range(start_hash[i]+1, end_hash[i]):
                    final_set.add(i + s[j] + i)
        return len(final_set)







if __name__ == '__main__':
    Solution().countPalindromicSubsequence(s="bbcbaba")