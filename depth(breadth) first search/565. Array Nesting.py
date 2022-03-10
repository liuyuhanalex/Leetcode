from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        max_count = 0
        hash_table = {}
        for i in range(len(nums)):
            rem_set = {nums[i]}
            index = nums[i]
            count = 1
            if hash_table.get(index) is not None:
                count += hash_table.get(index)
            else:
                while True:
                    pos = nums[index]
                    index = pos
                    if pos in rem_set:
                        break
                    rem_set.add(pos)
                    count += 1
            if count > max_count:
                max_count = count
        return max_count


if __name__ == '__main__':
    Solution().arrayNesting([5,4,0,3,1,6,2])