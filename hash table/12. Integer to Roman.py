

class Solution:
    def intToRoman(self, num: int) -> str:
        roman_dict = {
            12: 'I',
            11: 'IV',
            10: 'V',
            9: 'IX',
            8: 'V',
            7: 'XL',
            6: 'L',
            5: 'XC',
            4: 'C',
            3: 'CD',
            2: 'D',
            1: 'CM',
            0: 'M'
        }
        num_list = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        result_list = []
        for i in num_list:
            result_list.append(num // i)
            num = num % i
        res_str = ''
        for index, item in enumerate(result_list):
            num = item
            if num !=0:
                res_str += num * roman_dict.get(index)
        return res_str





if __name__ == '__main__':
    print(Solution().intToRoman(1994))