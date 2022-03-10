class Solution:
    def calculate(self, s: str) -> int:
        rec = []
        stack = []
        s = '(' + s + ')'
        for i in s:
            if i is '(':
                rec.append(len(stack))
            elif i is ')':
                last = rec.pop()
                new_num = self.cal(stack[last:])
                stack = stack[:last] + [new_num]
            else:
                stack.append(i)
        if len(stack) > 3:
            return self.cal(stack)
        else:
            return stack.pop()


    def cal(self, s):
        num = ''
        res = []
        s = [i for i in s if i != ' ']
        for index, i in enumerate(s):
            if i == ' ':
                continue
            if i != '+' and i != '-':
                num += i
            else:
                if len(num) > 0:
                    res.append(int(num))
                    num = ''
                res.append(i)
        if num != '':
            res.append(int(num))
        if res[0] != '-':
            res = ['+'] + res
        total = 0
        for index, i in enumerate(res):
            if i == '+':
                total += res[index+1]
            if i == '-':
                total -= res[index+1]
        return str(total)


if __name__ == '__main__':
    #print('result', Solution().calculate("-2+ 1"))
    print(Solution().calculate("1+1"))
