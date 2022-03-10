

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        res = ''
        pointer_a, pointer_b = len(a)-1, len(b)-1
        while pointer_a >= 0 or pointer_b>=0:
            inta = 0 if pointer_a < 0 else int(a[pointer_a])
            intb = 0 if pointer_b < 0 else int(b[pointer_b])
            total = inta + intb + carry
            if total >= 2:
                res = str(total%2) + res
                carry = 1
            else:
                res = str(total) + res
                carry = 0
            pointer_b -= 1
            pointer_a -= 1
        if carry == 1:
            res = '1' + res
        return res


if __name__ == '__main__':
    Solution().addBinary('111', '11')