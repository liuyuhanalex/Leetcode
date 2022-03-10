from typing import List
import re


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        conv_list = re.split(r'[-+\*]', expression)
        sigh_list = re.findall(r'[-+\*]', expression)
        pass


if __name__ == '__main__':
    Solution().diffWaysToCompute(expression="2-1+1*5")
