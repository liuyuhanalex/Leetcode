from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        i = len(digits) - 1
        while carry != 0:
            t_sum = digits[i] + carry
            if t_sum > 9:
                carry = t_sum//10
            else:
                carry = 0
            if i < 0:
                digits = [t_sum%10] + digits
                carry = 0
            else:
                digits[i] = t_sum%10
            i = i - 1
        return digits


if __name__ == '__main__':
    print(Solution().plusOne(digits=[9, 1, 9]))