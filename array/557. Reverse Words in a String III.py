class Solution:
    def reverseWords(self, s: str) -> str:
        word_list = s.split(' ')
        res = []
        for word in word_list:
            new_word = word[::-1]
            res.append(new_word)
        return ''.join(res)


if __name__ == '__main__':
    Solution().reverseWords(s="Let's take LeetCode contest")