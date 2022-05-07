from typing import List


class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        hash_table = {}
        for user, time, web in zip(username, timestamp, website):
            hash_table.setdefault(user, []).append((time, web))
        new_hash_table = {}
        for k, v in hash_table.items():
            v = [i[1] for i in sorted(v, key=lambda x: x[0])]
            print(v)
            if len(v) == 3:
                new_hash_table[','.join(v)] = new_hash_table.get(','.join(v), 0) + 1
            elif len(v) > 3:
                res = self.get_all_combination(v)
                for i in res:
                    new_hash_table[i] = new_hash_table.get(i, 0) + 1
            else:
                pass
        final_list = sorted(new_hash_table.items(), key=lambda x: (-x[1], x[0]))
        return final_list[0][0].split(',')

    def get_all_combination(self, ori_list):
        path = []
        res = set()
        def backtracking(index):
            if len(path) == 3:
                s = ','.join(path)
                res.add(s)
                return
            for index1, i in enumerate(ori_list[index:]):
                path.append(i)
                backtracking(index + index1 + 1)
                path.pop()
        backtracking(0)
        return res



if __name__ == '__main__':
    #Solution().mostVisitedPattern(username = ["ua","ua","ua","ub","ub","ub"], timestamp = [1,2,3,4,5,6], website = ["a","b","a","a","b","c"])
    #print(Solution().mostVisitedPattern(username = ["joe","joe","joe","james","james","james","james","mary", "mary","mary"], timestamp = [1,2,3,4,5,6,7,8,9,10], website = ["home","about","career","home","cart","maps","home","home","about","career"]))
    Solution().mostVisitedPattern(["h","eiy","cq","h","cq","txldsscx","cq","txldsscx","h","cq","cq"],
                                    [527896567,334462937,517687281,134127993,859112386,159548699,51100299,444082139,926837079,317455832,411747930],
                                ["hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","hibympufi","yljmntrclw","hibympufi","yljmntrclw"])
