from typing import List


class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        words_hash = {}
        for i in words:
            words_hash[i] = words_hash.get(i, 0) + 1
        cnt = 0
        whole_set = set(words_hash.keys())
        for i in words:
            if words_hash[i] > 0:
                words_hash[i] = words_hash[i] - 1
                if words_hash[i] == 0:
                    whole_set.remove(i)
                if words_hash.get(i[::-1], 0) > 0:
                    cnt += 4
                    words_hash[i[::-1]] = words_hash[i[::-1]] - 1
                    if words_hash[i[::-1]] == 0:
                        whole_set.remove(i[::-1])
                else:
                    words_hash[i] = words_hash[i] + 1
                    whole_set.add(i)
        if len(whole_set) > 0 and len([i for i in whole_set if i[0] == i[1]]) > 0:
            cnt += 2
        return cnt


if __name__ == '__main__':
    #Solution().longestPalindrome(words = ["lc","cl","gg"])
    print(Solution().longestPalindrome(["em","pe","mp","ee","pp","me","ep","em","em","me"]))