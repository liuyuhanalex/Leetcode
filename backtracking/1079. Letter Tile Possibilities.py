

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        res = []
        def backtracking(choices, path):
            seen = set()
            if path not in res and len(path) > 0:
                res.append(path)
            for index, i in enumerate(choices):
                if i not in seen:
                    seen.add(i)
                    path += i
                    new_choices = choices[:index]+choices[index+1:]
                    backtracking(new_choices, path)
                    path = path[:-1]
        init_choices = list(tiles)
        backtracking(init_choices, '')
        return len(res)

if __name__ == '__main__':
    Solution().numTilePossibilities('AAB')