class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_list = list(num1)
        num2_list = list(num2)
        total = 0
        res = ''
        while total or num1_list or num2_list:
            if num1_list:
                total += int(num1_list.pop())
            if num2_list:
                total += int(num2_list.pop())
            res += str(total%10)
            total //= 10
        return res[::-1]




if __name__ == '__main__':
    print(Solution().addStrings(num1 = "456", num2 = "77"))