from typing import List


class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        queue = [(sr, sc)]
        ori_color = image[sr][sc]
        finish_set = set()
        while len(queue) != 0:
            r, c = queue.pop()
            image[r][c] = newColor
            if r-1 >= 0 and image[r-1][c] == ori_color and (r-1,c) not in finish_set:
                queue.append((r-1, c))
                finish_set.add((r-1,c))
                image[r-1][c] = newColor
            if r+1 <= len(image)-1 and image[r+1][c] == ori_color and (r+1, c) not in finish_set:
                queue.append((r + 1, c))
                finish_set.add((r + 1, c))
                image[r + 1][c] = newColor
            if c - 1 >=0 and image[r][c-1] == ori_color and (r, c-1) not in finish_set:
                queue.append((r, c-1))
                finish_set.add((r, c-1))
                image[r][c-1] = newColor
            if c+1 <= len(image[0])-1 and image[r][c+1] == ori_color and (r, c+1) not in finish_set:
                queue.append((r, c+1))
                finish_set.add((r, c+1))
                image[r][c+1] = newColor
        return image

    def floodFill_ans(self, image, sr, sc, newColor):
        R, C = len(image), len(image[0])
        color = image[sr][sc]
        if color == newColor: return image

        def dfs(r, c):
            if image[r][c] == color:
                image[r][c] = newColor
                if r >= 1: dfs(r - 1, c)
                if r + 1 < R: dfs(r + 1, c)
                if c >= 1: dfs(r, c - 1)
                if c + 1 < C: dfs(r, c + 1)
        dfs(sr, sc)
        return image

if __name__ == '__main__':
    Solution().floodFill_ans([[1, 1, 1], [1, 1, 0], [1, 0, 1]], sr=1, sc=1, newColor=2)
