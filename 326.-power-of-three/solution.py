from testcase import testcase


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1:
            return True
        n /= 3
        if n < 1:
            return False
        return self.isPowerOfThree(n)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.isPowerOfThree(t) == expected


if __name__ == "__main__":
    s = Solution()
