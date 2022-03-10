

class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(' ', '')
        s = s + '!'
        stack = []
        i = 0
        while i < len(s):
            new_s = ''
            while s[i] not in ['+', '-', '*', '/', '!']:
                new_s += s[i]
                i += 1
            num = int(new_s)
            print(s[i])
            i += 1
            print(num)










if __name__ == '__main__':
    Solution().calculate(s = " 33 * 5 + 2 ")