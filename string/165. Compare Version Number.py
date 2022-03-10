class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1, version2 = version1.split('.'), version2.split('.')
        if len(version1) > len(version2):
            version2 = version2 + [0] * (len(version1) - len(version2))
        elif len(version2) > len(version1):
            version1 = version1 + [0] * (len(version2) - len(version1))
        for v1, v2 in zip(version1, version2):
            if int(v1) == 0:
                v1 = 0
            else:
                v1 = int(v1.lstrip('0'))
            if int(v2) == 0:
                v2 = 0
            else:
                v2 = int(v2.lstrip('0'))
            if v1 > v2:
                return 1
            elif v1 < v2:
                return -1
            else:
                continue
        return 0


if __name__ == '__main__':
    print(Solution().compareVersion(version1 = "1.0", version2 = "1.0.0"))