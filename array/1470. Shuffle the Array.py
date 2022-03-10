from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        pointer1, pointer2 = 0, n
        final_res =[]
        while pointer2 < len(nums) -1 or pointer1 < n:
            if pointer1 < n:
                final_res.append(nums[pointer1])
                pointer1 += 1
            if pointer2 <= len(nums) -1:
                final_res.append(nums[pointer2])
                pointer2 += 1
        return final_res



if __name__ == '__main__':
    Solution().shuffle(nums = [1,2,3,4,4,3,2,1], n = 4)