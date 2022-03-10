class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        real1, imaginary1 = num1.split('+')
        real2, imaginary2 = num2.split('+')
        r_real = int(real1) * int(real2) + int(imaginary1[:-1]) * int(imaginary2[:-1])*(-1)
        imaginary = int(real1) * int(imaginary2[:-1]) + int(real2) * int(imaginary1[:-1])
        return str(r_real) + '+' + str(imaginary) + 'i'



if __name__ == '__main__':
    print(Solution().complexNumberMultiply(num1 = "1+-1i", num2 = "1+-1i"))