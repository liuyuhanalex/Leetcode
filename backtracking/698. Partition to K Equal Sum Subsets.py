from typing import List
from copy import deepcopy


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 回溯的解决方法
        if sum(nums) % k != 0:
            return False
        p_sum = sum(nums) // k
        whole_list = [0 for _ in range(k)]
        res = []
        nums = sorted(nums, reverse=True)
        def backtracking(index):
            if len(res) > 0:
                return
            if index > len(nums) - 1:
                if set(whole_list).pop() == p_sum:
                    res.append(1)
                return
            for i in range(k):
                if whole_list[i] + nums[index] <= p_sum:
                    whole_list[i] = whole_list[i] + nums[index]
                    backtracking(index+1)
                    whole_list[i] = whole_list[i] - nums[index]
        backtracking(0)
        if len(res) > 0:
            return True
        return False








if __name__ == '__main__':
    print(Solution().canPartitionKSubsets(nums = [730,580,401,659,5524,405,1601,3,383,4391,4485,1024,1175,1100,2299,3908], k = 4))