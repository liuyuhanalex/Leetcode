class Solution:
    def originalDigits(self, s: str) -> str:
        show_dict = {'x': ['s', 'i'],
                     'g': ['e','i','g','h','t'],
                     'z': ['e', 'r', 'o'],
                     'w': ['t', 'o'],
                     'u': ['f', 'o', 'r'],
                     's': ['e', 'e', 'v', 'n'],
                     'v': ['f', 'i', 'e'],
                     'i': ['n', 'n' , 'e'],
                     't': ['h', 'r', 'e', 'e'],
                     'o': ['n', 'e']}
        num_dict = {
            'x': 6,
            'u': 4,
            'g': 8,
            'w': 2,
            'z': 0,
            's': 7,
            'v': 5,
            'i': 9,
            't': 3,
            'o': 1
        }
        hash_table = {}
        for i in s:
            hash_table[i] = hash_table.get(i, 0) + 1
        res = []
        for char in ['x', 'u', 'g', 'w', 'z', 's', 'v', 'i', 't', 'o']:
            if hash_table.get(char, 0) > 0:
                num = hash_table.get(char)
                hash_table[char] = hash_table.get(char) - num
                for c in show_dict.get(char):
                    hash_table[c] = hash_table.get(c) - num
                res += [num_dict.get(char)] * num
        return ''.join([str(i) for i in sorted(res)])



if __name__ == '__main__':
    print(Solution().originalDigits(s = "owoztneoer"))