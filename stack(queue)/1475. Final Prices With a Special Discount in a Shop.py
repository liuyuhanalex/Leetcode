from typing import List
from copy import copy

class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        stack = []
        res = copy(prices)
        for i in range(len(prices)):
            if not stack or prices[i] > prices[stack[-1]]:
                stack.append(i)
            else:
                while stack and prices[i] <= prices[stack[-1]]:
                    index = stack.pop()
                    res[index] = prices[index]-prices[i]
                stack.append(i)
        return res





if __name__ == '__main__':
    print(Solution().finalPrices(prices = [10,1,1,6]))