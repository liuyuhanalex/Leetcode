
class Solution:
    def countCollisions(self, directions: str) -> int:
        s = ''.join(directions)
        return len([i for i in s.lstrip('L').rstrip('R') if i != 'S'])



if __name__ == '__main__':
    Solution().countCollisions(directions = "RLRSLL")