class Solution:
    def numTrees(self, n: int) -> int:
        memory_dict = {}
        def get_num_of_trees(nums):
            if len(nums) == 2:
                return 2
            if len(nums) == 0 or len(nums) == 1:
                return 1
            if memory_dict.get((nums[0], len(nums))) is not None:
                return memory_dict.get((nums[0], len(nums)))
            total = 0
            for i in range(len(nums)):
                total += get_num_of_trees(nums[:i]) * get_num_of_trees(nums[i+1:])
            memory_dict[(nums[0], len(nums))] = total
            return total
        init_list = [i for i in range(1, n+1)]
        return get_num_of_trees(init_list)


if __name__ == '__main__':
    print(Solution().numTrees(19))