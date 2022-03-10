import numpy as np

class Solution:
    def maximumSwap(self, num: int) -> int:
        re_list = list(str(num))
        for i in range(len(re_list)-1):
            cur_num = int(re_list[i])
            max_num = max([int(re_list[j]) for j in range(i+1, len(re_list))])
            if max_num > cur_num:
                pos = len(re_list) - 1
                for z in range(len(re_list)-1, i, -1):
                    if re_list[z] == str(max_num):
                        break
                    pos -= 1
                re_list[pos] = cur_num
                re_list[i] = max_num
                return int(''.join([str(x) for x in re_list]))
        return num


if __name__ == '__main__':
    print(Solution().maximumSwap(num = 1993))