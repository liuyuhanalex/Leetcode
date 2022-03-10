from typing import List
import numpy as np


class Solution:
    def jump(self, nums: List[int]) -> int:
        reach_max = 0
        step = 0
        start, end = 0, 0
        while reach_max < len(nums)-1:
            array = [i+x+start for i, x in enumerate(nums[start:end+1])] + [0]
            reach_max = max(array)
            start = np.argmax(array)
            end = reach_max
            step += 1
        return step



if __name__ == '__main__':
    print(Solution().jump([7,0,9,6,9,6,1,7,9,0,1,2,9,0,3]))