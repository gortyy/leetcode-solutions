from testcase import testcase


class Solution:
    def hammingWeight(self, n: int) -> int:
        return sum(int(x) for x in bin(n)[2:])


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.hammingWeight(t) == expected


if __name__ == "__main__":
    s = Solution()
