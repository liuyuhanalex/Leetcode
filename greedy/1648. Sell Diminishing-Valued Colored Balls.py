from typing import List


class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        max_num, min_num = 10**9, 0
        while max_num > min_num:
            mid = (max_num + min_num) / 2
            total_sum = 0
            for i in inventory:
                if i > mid:
                    total_sum += i - mid
            if total_sum > orders:
                min_num = mid + 1
            else:
                max_num = mid
        total_sum = 0
        for i in inventory:
            if i > min_num:
                total_sum += (i+min_num+1)*(i-min_num)/2
                orders -= (i-min_num)
        total_sum += orders * min_num
        return total_sum % 10**9 + 7




if __name__ == '__main__':
    print(Solution().maxProfit(inventory = [1000000000], orders = 1000000000))
    print(773160767 - 252264991)
    print(((520895776 + 773160767) * 252264991 // 2) % (10**9 + 7))