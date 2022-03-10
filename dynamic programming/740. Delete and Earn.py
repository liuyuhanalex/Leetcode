from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        re_dict = {}
        for i in nums:
            re_dict[i] = re_dict.get(i, 0) + i
        re_list = sorted(re_dict.keys())
        ans_list = [[0, re_dict.get(re_list[0])]]
        for index, i in enumerate(re_list[1:]):
            if re_list[index] == i-1:
                earn_without = max(ans_list[-1][1], ans_list[-1][0])
                earn_with = ans_list[-1][0] + re_dict.get(i)
            else:
                earn_without = max(ans_list[-1][1], ans_list[-1][0])
                earn_with = earn_without + re_dict.get(i)
            ans_list.append([earn_without, earn_with])
        return max(ans_list[-1][0], ans_list[-1][1])



if __name__ == '__main__':
    Solution().deleteAndEarn([10,8,4,2,1,3,4,8,2,9,10,4,8,5,9,1,5,1,6,8,1,1,6,7,8,9,1,7,6,8,4,5,4,1,5,9,8,6,10,6,4,3,8,4,10,8,8,10,6,4,4,4,9,6,9,10,7,1,5,3,4,4,8,1,1,2,1,4,1,1,4,9,4,7,1,5,1,10,3,5,10,3,10,2,1,10,4,1,1,4,1,2,10,9,7,10,1,2,7,5])
