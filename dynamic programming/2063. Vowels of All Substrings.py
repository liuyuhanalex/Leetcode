class Solution:
    def countVowels(self, word: str) -> int:
        vowel_set = {'a', 'e', 'i', 'o', 'u'}
        sum_num = 0
        N = len(word)
        for i in range(len(word)):
            if word[i] in vowel_set:
                sum_num += (i+1)*(N-i)
        return sum_num

if __name__ == '__main__':
    Solution().countVowels('aba')