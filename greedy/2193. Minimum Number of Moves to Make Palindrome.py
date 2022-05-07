

class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        start, end = 0, len(s) - 1
        s = list(s)
        cnt = 0
        while start < end:
            if s[start] != s[end]:
                right_probe = start
                while right_probe < end and s[right_probe] != s[end]:
                    right_probe += 1
                right_dist = right_probe - start
                left_probe = end
                while left_probe > start and s[left_probe] != s[start]:
                    left_probe -= 1
                left_dist = end - left_probe
                if right_dist > left_dist:
                    if left_probe + 1 == end:
                        s[left_probe] = s[end]
                    else:
                        s[left_probe:end] = s[left_probe+1:end+1]
                    s[end] = s[start]
                    cnt += left_dist
                else:
                    if right_probe - 1 == start:
                        s[right_probe] = s[start]
                    else:
                        s[start + 1: right_probe + 1] = s[start: right_probe]
                    s[start] = s[end]
                    cnt += right_dist
            start += 1
            end -= 1
        return cnt


if __name__ == '__main__':
    #Solution().minMovesToMakePalindrome("letelt")
    #print(Solution().minMovesToMakePalindrome('aabb'))
    print(Solution().minMovesToMakePalindrome('skwhhaaunskegmdtutlgtteunmuuludii'))