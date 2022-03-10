class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digit = 0
        res = []
        for i in reversed(num1):
            i_int = int(i)
            carry = 0
            j = len(num2) - 1
            total = ''
            while carry or j >= 0:
                j_int = 0
                if j >=0: j_int = int(num2[j])
                total = str((i_int * j_int + carry) % 10) + total
                carry = (i_int * j_int + carry) // 10
                j -= 1
            res.append(total + digit*'0')
            digit += 1
        return sum([int(i) for i in res])









if __name__ == '__main__':
    Solution().multiply(num1 = "123", num2 = "456")
