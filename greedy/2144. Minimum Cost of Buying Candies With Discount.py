from typing import List

class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        sorted_list = sorted(cost, reverse=True)
        cost_cnt = 0
        while sorted_list:
            cost_cnt += sorted_list.pop(0)
            if sorted_list:
                cost_cnt += sorted_list.pop(0)
            if sorted_list:
                sorted_list.pop(0)
        return cost_cnt