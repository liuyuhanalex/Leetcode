


class Solution:
    def romanToInt(self, s: str) -> int:
        # I             1
        # V             5
        # X             10
        # L             50
        # C             100
        # D             500
        # M             1000
        roman_dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        length = len(s)
        sum_count = 0
        for index, i in enumerate(s):
            if i == 'I' and index < length - 1 and (s[index+1] == 'X' or s[index+1] == 'V'):
                num = -1
            elif i == 'X' and index < length - 1 and (s[index+1] == 'L' or s[index+1] == 'C'):
                num = -10
            elif i == 'C' and index < length - 1 and (s[index+1] == 'D' or s[index+1] == 'M'):
                num = -100
            else:
                num = roman_dict.get(i)
            sum_count += num
        return sum_count


if __name__ == '__main__':
    print(Solution().romanToInt("III"))
