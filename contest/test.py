from typing import List

class Solution:
    def minimalKSum(self, nums: List[int], k: int) -> int:
        sorted_num = sorted(set(nums))
        sorted_num = [0] + sorted_num
        res = 0
        for i in range(1, len(sorted_num)):
            if k > 0:
                num_num = sorted_num[i] - sorted_num[i - 1] - 1
                if num_num > 0:
                    if num_num == 1:
                        res += sorted_num[i-1] + 1
                        k -= num_num
                        continue
                    if k - num_num >= 0:
                        res += ((sorted_num[i-1] + sorted_num[i]) * num_num) // 2
                    else:
                        res += (sorted_num[i - 1] + 1 + sorted_num[i - 1] + k) * k // 2
                k -= num_num
            else:
                break
        if k > 0:
            if k == 1:
                res += sorted_num[-1] + 1
            else:
                res += (sorted_num[-1] + 1 + sorted_num[-1]+k) * k //2
        return res

if __name__ == '__main__':
    #print(Solution().minimalKSum([1,4,25,10,25], 2))
    print(Solution().minimalKSum([1000000000], 1000000000))