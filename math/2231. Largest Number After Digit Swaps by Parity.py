class Solution:
    def largestInteger(self, num: int) -> int:
        pos_list = []
        even_list = []
        odd_list = []
        for i in list(str(num)):
            if int(i) % 2 == 0:
                pos_list.append(0)
                even_list.append(i)
            else:
                pos_list.append(1)
                odd_list.append(i)
        even_list = sorted(even_list)
        odd_list = sorted(odd_list)
        final_str = ''
        for i in pos_list:
            if i == 0:
                final_str += even_list.pop()
            else:
                final_str += odd_list.pop()
        return int(final_str)




if __name__ == '__main__':
    print(Solution().largestInteger(num = 1234))