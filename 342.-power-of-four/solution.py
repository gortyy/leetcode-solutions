from testcase import testcase


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1:
            return True
        num /= 4
        if num < 1:
            return False
        return self.isPowerOfFour(num)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.isPowerOfFour(t) == expected


if __name__ == "__main__":
    s = Solution()
