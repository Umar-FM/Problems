# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        l=1
        r=n
        while l<=r:
            m=(l+r)//2
            if isBadVersion(m):
                if not isBadVersion(m-1): return m
                else:
                    r=m-1
            else:
                if isBadVersion(m+1): return m+1
                else:
                    l=m+1
                    