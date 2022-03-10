from typing import List


class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        threes = set([str(i*3) for i in range(1, n//3 + 1)])
        fives = set([str(i*5) for i in range(1, n//5 + 1)])
        res = []
        for i in range(1, n+1):
            if str(i) in threes and str(i) in fives:
                res.append('FizzBuzz')
            elif str(i) in threes:
                res.append('Fizz')
            elif str(i) in fives:
                res.append('Buzz')
            else:
                res.append(str(i))
        return res


if __name__ == '__main__':
    Solution().fizzBuzz(15)