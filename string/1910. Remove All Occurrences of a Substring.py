

class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        last_s = s
        while s:
            s = s.replace(part, '', 1)
            if s == last_s:
                break
            last_s = s
        return s



if __name__ == '__main__':
    Solution().removeOccurrences(s = "axxxxyyyyb", part = "xy")