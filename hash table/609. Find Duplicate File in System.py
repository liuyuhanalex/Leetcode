from typing import List
import re


class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_dict = {}
        for i in paths:
            root, *files = i.split(' ')
            for f in files:
                name, content = f.split('(')
                full_path = root + '/' + name
                content = content[:-1]
                content_dict[content] = content_dict.get(content, []) + [full_path]
        final_res = []
        for key, value in content_dict.items():
            if len(value) >= 2:
                final_res.append(value)
        return final_res


if __name__ == '__main__':
    Solution().findDuplicate(paths = ["root/a 1.txt(abcd) 2.txt(efgh)","root/c 3.txt(abcd)","root/c/d 4.txt(efgh)","root 4.txt(efgh)"])