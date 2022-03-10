# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

def isBadVersion(self):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo, hi = 1, n
        while lo <= hi:
            mid = (lo + hi) // 2

            if isBadVersion(mid):
                hi = mid - 1
            else:
                lo = mid + 1
        return lo


if __name__ == '__main__':
    Solution().firstBadVersion(n=5)
