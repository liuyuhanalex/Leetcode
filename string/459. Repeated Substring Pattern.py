class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        for i in range(len(s)//2):
            ss = s[:i+1]
            times = len(s)//len(ss)
            if ss*times == s:
                return True
        return False


if __name__ == '__main__':
    Solution().repeatedSubstringPattern(s="abcabcabcabc")