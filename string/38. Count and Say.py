
class Solution:
    def countAndSay(self, n: int) -> str:
        first, res = '1', '1'
        def say(s: str):
            fix_char = s[0]
            count = 1
            result = ""
            for i in range(1, len(s)):
                if s[i] == fix_char:
                    count += 1
                else:
                    result += str(count) + fix_char
                    fix_char, count = s[i], 1
            result += str(count) + fix_char
            return result
        for i in range(1, n):
            res = say(first)
            first = res
        return res



if __name__ == '__main__':
    print(Solution().countAndSay(6))