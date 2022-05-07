from typing import List

class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        after_sum = sum(nums)
        length = len(nums)
        pre_sum = 0
        pre_len = 1
        min_dif = 100000
        min_index = 0
        for i in nums:
            pre_sum += i
            after_sum -= i
            try:
                dif = abs(pre_sum//pre_len - after_sum//(length - pre_len))
            except Exception as ex:
                dif = abs(pre_sum // pre_len)
            if dif < min_dif:
                min_dif = dif
                min_index = pre_len - 1
            pre_len += 1
        return min_index




if __name__ == '__main__':
    print(Solution().minimumAverageDifference(nums = [2,5,3,9,5,3]))
    print(Solution().minimumAverageDifference([0,1,0,1,0,1]))
