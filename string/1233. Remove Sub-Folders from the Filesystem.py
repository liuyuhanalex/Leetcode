from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        new_list = [(i, len(i.split('/'))) for i in folder]
        res_set = set()
        for i in sorted(new_list, key=lambda x: x[1]):
            path_list = i[0].split('/')
            flag = True
            for j in res_set:
                j_list = j.split('/')
                if path_list[:len(j_list)] == j_list:
                    flag = False
                    break
            if flag:
                res_set.add(i[0])
        return list(res_set)





if __name__ == '__main__':
    print(Solution().removeSubfolders(folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]))
    print(Solution().removeSubfolders(["/a/a","/a/ab"]))