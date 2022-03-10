from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            num = i
            flag = False
            while stack and num <0 and stack[-1] > 0:
                out = stack.pop()
                if num == -out:
                    flag = True
                    break
                elif abs(num) < abs(out):
                    num = out
                else:
                    num = num
            if not flag:
                stack.append(num)
        return stack


if __name__ == '__main__':
    Solution().asteroidCollision([-2,-1,1,2])