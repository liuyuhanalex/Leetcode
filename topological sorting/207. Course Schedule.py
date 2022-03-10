from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_nums = [0] * numCourses
        hash_table = {}
        for i in prerequisites:
            in_nums[i[1]] = in_nums[i[1]] + 1
            hash_table.setdefault(i[0], []).append(i[1])
        q = [index for index, i in enumerate(in_nums) if i == 0]
        if len(q) == 0:
            return False
        cnt = 0
        while q:
            num = q.pop(0)
            cnt += 1
            for i in hash_table.get(num):
                in_nums[i] = in_nums[i] - 1
                if in_nums[i] == 0:
                    q.append(i)
        return cnt == numCourses







if __name__ == '__main__':
    Solution().canFinish(numCourses = 2, prerequisites = [[1,0],[0,1]])
