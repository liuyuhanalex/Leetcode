class Solution:
    def reverseWords(self, s: str) -> str:
        str_list = [i for i in s.split(' ') if len(i) > 0]
        res = ''
        for s in reversed(str_list):
            res += s + ' '
        return res





if __name__ == '__main__':
    print(Solution().reverseWords('a good   example'))