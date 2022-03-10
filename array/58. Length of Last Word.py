class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = [i for i in s.split(' ') if len(i) > 0]
        return len(words[-1])


if __name__ == '__main__':
    Solution().lengthOfLastWord("   fly me   to   the moon  ")