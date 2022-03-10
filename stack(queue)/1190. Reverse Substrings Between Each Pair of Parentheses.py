class Solution:
    def reverseParentheses(self, s: str) -> str:
        res = []
        pos = []
        s = list(s)
        for index, i in enumerate(s):
            if i != '(' and i!= ')':
                res.append(s[index])
            elif i == '(':
                pos.append(len(res))
            else:
                num = pos.pop()
                res[num:] = res[num:][::-1]
        return ''.join(res)




"""
这道题给了一个只含有小写字母和括号的字符串s，现在让从最内层括号开始，
每次都反转括号内的所有字符，然后可以去掉该内层括号，依次向外层类推，直到去掉所有的括号为止。
可能有的童鞋拿到题后第一反应可能是递归到最内层，翻转，然后再一层一层的出来。
这样的做的话就有点麻烦了，而且保不齐还有可能超时。
比较好的做法就是直接遍历这个字符串，当遇到字母时，
将其加入结果 res，当遇到左括号时，将当前 res 的长度加入一个数组 pos，
当遇到右括号时，取出 pos 数组中的最后一个数字，并翻转 res 中该位置到结尾的所有字母，
因为这个区间刚好就是当前最内层的字母，这样就能按顺序依次翻转所有括号中的内容，最终返回结果 res 即可
"""

if __name__ == '__main__':
    print(Solution().reverseParentheses(s="(ed(et(oc))el)"))
