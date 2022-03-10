from typing import List


class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        common_res = set(list1).intersection(set(list2))
        dict_1, dict_2 = {}, {}
        for index, i in enumerate(list1):
            dict_1[i] = index
        for index, i in enumerate(list2):
            dict_2[i] = index
        res = {}
        for i in common_res:
            dist = dict_1.get(i) + dict_2.get(i)
            res[dist] = res.get(dist, []) + [i]
        min_dist = min([i for i in res.keys()])
        return res.get(min_dist)


if __name__ == '__main__':
    Solution().findRestaurant(list1 = ["Shogun","Tapioca Express","Burger King","KFC"], list2 = ["KNN","KFC","Burger King","Tapioca Express","Shogun"])