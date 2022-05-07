class Solution:
    def minimumSum(self, num: int) -> int:
        num_list = [i for i in str(num) if i != '0']
        sorted_list = sorted(num_list)
        num1, num2 = '0', '0'
        num1 += ''.join(sorted_list[0::2])
        num2 += ''.join(sorted_list[1::2])
        return int(num1) + int(num2)


if __name__ == '__main__':
    Solution().minimumSum(num = 2932)
