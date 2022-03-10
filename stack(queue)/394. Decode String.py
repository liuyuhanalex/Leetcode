num_set = {'0', '1', '2', '3', '4', '5','6','7','8','9'}


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        res = []
        for i in range(len(s)):
            if s[i] == '[':
                stack.append(len(res))
            elif s[i] == ']':
                start = stack.pop()
                str_l = ''.join(res[start:])
                res = res[:start]
                num = ''
                while res and res[-1] in num_set:
                    if stack and len(res) <= stack[-1]:
                        break
                    num = res.pop() + num
                res.append(str_l*int(num))
            else:
                res.append(s[i])
        return ''.join(res)




if __name__ == '__main__':
    Solution().decodeString("3[a2[c]]")
    #print(Solution().decodeString("3[a]2[bc]"))
    #print(Solution().decodeString("100[leetcode]"))
    print(Solution().decodeString("3[z]2[2[y]pq4[2[jk]e1[f]]]ef"))