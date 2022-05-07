from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        hash_table_odd = {}
        hash_table_even = {}
        for index, i in enumerate(nums):
            if index % 2 == 0:
                hash_table_odd[i] = hash_table_odd.get(i, 0) + 1
            else:
                hash_table_even[i] = hash_table_even.get(i, 0) + 1
        sorted_list_odd = sorted(hash_table_odd.items(), key=lambda x: x[1], reverse=True)
        sorted_list_even = sorted(hash_table_even.items(), key=lambda x: x[1], reverse=True)
        sorted_list_even.append((0, 0))
        sorted_list_odd.append((0, 0))
        if sorted_list_even[0][0] != sorted_list_odd[0][0]:
            total =len(nums) // 2 - sorted_list_odd[0][1] + len(nums) - len(nums)//2 - sorted_list_even[0][1]
        else:
            total = min(len(nums) // 2 - sorted_list_odd[0][1] + len(nums) - len(nums)//2 - sorted_list_even[1][1],
                        len(nums) // 2 - sorted_list_odd[1][1] + len(nums) - len(nums)//2 - sorted_list_even[0][1])
        return total



if __name__ == '__main__':
    #print(Solution().minimumOperations(nums = [3,1,3,2,4,3]))
    print(Solution().minimumOperations([1,2,2,2,2]))