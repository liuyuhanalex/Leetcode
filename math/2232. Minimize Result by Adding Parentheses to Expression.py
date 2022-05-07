
class Solution:
    def minimizeResult(self, expression: str) -> str:
        num1, num2 = expression.split('+')
        num1_pair, num2_pair = [['1', num1, 0]], [[num2, '1', len(num2)]]
        for i in range(len(num1)-1):
            num1_pair.append([num1[:i+1], num1[i+1:], i+1])
        for i in range(len(num2) - 1):
            num2_pair.append([num2[:i+1], num2[i+1:], i+1])
        min_total = 10000000000
        final = []
        for i in num1_pair:
            for j in num2_pair:
                total = int(i[0]) * (int((i[1])) + int(j[0])) * int(j[1])
                if total < min_total:
                    min_total = total
                    final = [i[2], j[2]]

        expression = num1[:final[0]] + '(' + num1[final[0]:] + '+' + num2[:final[1]] + ')' + num2[final[1]:]
        return expression




if __name__ == '__main__':
    print(Solution().minimizeResult(expression = "99999999+9"))