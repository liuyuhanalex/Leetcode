class Solution:
    def lastRemaining(self, n: int) -> int:
        if n == 1:
            return 1
        n_list = list(range(n+1))[1:]
        flag = 1
        while len(n_list) > 1:
            if flag == 1:
                cut_list = n_list[::2]
                n_list = [i for i in n_list if i not in cut_list]
            else:
                cut_list = n_list[::-1][::2]
                n_list = [i for i in n_list if i not in cut_list]
            flag = 1 - flag
        return n_list[0]


if __name__ == '__main__':
    for i in range(1, 100):
        print(i, Solution().lastRemaining(i))