
class Solution:
    def simplifyPath(self, path: str) -> str:
        """

        :rtype: object
        """
        queue = []
        op_list = path.split('/')
        for i in op_list:
            if len(i) > 0:
                if i == '.':
                    pass
                elif i == '..':
                    queue.pop()
                else:
                    queue.append(i)
        return '/'+ '/'.join(queue)


if __name__ == '__main__':
    print(Solution().simplifyPath("/a/./b/../../c/"))