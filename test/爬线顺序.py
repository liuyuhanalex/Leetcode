from copy import copy

if __name__ == '__main__':
    path = []
    res = []
    def backtracking():
        if len(path) == 10:
            res.append(copy(path))
            return
        for i in [1, 2]:
            if len(path) < 3 or path[-1:-4:-1] != [i, i, i]:
                path.append(i)
                backtracking()
                path.pop()
    backtracking()
    print("可能的爬线顺序一共有:{} 种".format(len(res)))