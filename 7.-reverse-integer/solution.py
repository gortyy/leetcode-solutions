from testcase import testcase


class Solution:
    def reverse(self, x: int) -> int:
        negate = x < 0
        reversed = int(str(abs(x))[::-1])
        if negate:
            return -reversed
        return reversed


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.reverse(t) == expected


if __name__ == "__main__":
    s = Solution()
