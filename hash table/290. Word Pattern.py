class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_list = s.split(" ")
        if len(s_list) != len(pattern):
            return False
        hash_table = {}
        seen_set = set()
        for i in range(len(s_list)):
            if hash_table.get(pattern[i]) is None:
                if s_list[i] in seen_set:
                    return False
                hash_table[pattern[i]] = s_list[i]
                seen_set.add(s_list[i])
            else:
                if hash_table.get(pattern[i]) != s_list[i]:
                    return False
        return True


if __name__ == '__main__':
    Solution().wordPattern(pattern = "aaaa", s = "dog cat cat dog")