from typing import List


class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums) % k !=0:
            return False
        num_dict = {}
        for i in nums:
            num_dict[i] = num_dict.get(i, 0) + 1
        nums = sorted(nums)
        for i in nums:
            if num_dict.get(i, 0) == 0: continue
            num_dict[i] = num_dict[i] - 1
            for j in range(1, k):
                if num_dict.get(i+j, 0) == 0:
                    return False
                else:
                    num_dict[i+j] = num_dict[i+j] - 1
        return True



if __name__ == '__main__':
    print(Solution().isPossibleDivide(nums=[3,2,1,2,3,4,3,4,5,9,10,11], k=3))