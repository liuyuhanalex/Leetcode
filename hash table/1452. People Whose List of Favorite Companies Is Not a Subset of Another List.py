from typing import List


class Solution:
    def peopleIndexes(self, favoriteCompanies: List[List[str]]) -> List[int]:
        res = []
        for index in range(len(favoriteCompanies)):
            for j in range(len(favoriteCompanies)):
                if j != index and len(favoriteCompanies[j]) >= len(favoriteCompanies[index]):
                    if len(set(favoriteCompanies[j]).intersection(set(favoriteCompanies[index]))) == len(set(favoriteCompanies[index])):
                        res.append(index)
                        break
        return [i for i in range(len(favoriteCompanies)) if i not in res]



if __name__ == '__main__':
    Solution().peopleIndexes(favoriteCompanies = [["leetcode","google","facebook"],["google", "microsoft"],["google","facebook"],["google"],["amazon"]])
