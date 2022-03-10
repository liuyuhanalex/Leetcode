from typing import List

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        for i in range(left, right+1):
            num = i
            flag = False
            while num > 0:
                digit = num%10
                if digit==0 or i % digit !=0:
                    flag = True
                    break
                else:
                    num //=10
            if not flag:
                res.append(i)
        return res



if __name__ == '__main__':
    Solution().selfDividingNumbers(left = 1, right = 22)