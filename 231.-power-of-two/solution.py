from testcase import testcase


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1:
            return True
        n /= 2
        if n < 1:
            return False
        return self.isPowerOfTwo(n)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.isPowerOfTwo(t) == expected


if __name__ == "__main__":
    s = Solution()
