class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        note_dict = {}
        for i in ransomNote:
            note_dict[i] = note_dict.get(i, 0) + 1
        magaz_dict = {}
        for i in magazine:
            magaz_dict[i] = magaz_dict.get(i, 0) + 1
        for k, v in note_dict.items():
            if magaz_dict.get(k) is None or magaz_dict.get(k) < v:
                return False
        return True


if __name__ == '__main__':
    print(Solution().canConstruct(ransomNote="aa", magazine="aab"))
