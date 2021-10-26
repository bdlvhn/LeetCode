# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        global first
        first = n + 1

        def binSearch(left: int, right: int):
            global first
            if left > right:
                return

            mid = (left + right) // 2
            if isBadVersion(mid):
                first = mid
                binSearch(left, mid - 1)
            else:
                binSearch(mid + 1, right)

        binSearch(1, n)
        return first
        