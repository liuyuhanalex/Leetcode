class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s1_dict = [0]*26
        s2_dict = [0]*26
        if s1_len > len(s2):
            return False
        for i, j in zip(s1, s2[:s1_len]):
            s1_dict[ord(i)-97] += 1
            s2_dict[ord(j) - 97] += 1
        if s2_dict == s1_dict:
            return True
        for i in range(s1_len, len(s2)):
            s2_dict[ord(s2[i]) - 97] += 1
            s2_dict[ord(s2[i-s1_len]) - 97] -= 1
            if s2_dict == s1_dict:
                return True
        return False


if __name__ == '__main__':
    print(Solution().checkInclusion("ab", "a"))