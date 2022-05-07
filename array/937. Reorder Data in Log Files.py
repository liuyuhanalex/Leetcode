from typing import List
import re


class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dig_list = []
        let_list = []
        for i in logs:
            try:
                num = int(i.split(' ')[1])
                dig_list.append(i)
            except:
                num, content = i.split(' ', 1)
                let_list.append((num, content))
        let_list = sorted(let_list, key=lambda x: (x[1],x[0]))
        final_list = [i[0] + ' ' + i[1] for i in let_list] + dig_list
        return final_list


if __name__ == '__main__':
    print(Solution().reorderLogFiles(logs=["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]))