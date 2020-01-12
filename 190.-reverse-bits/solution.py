from testcase import testcase


class Solution:
    def reverseBits(self, n: int) -> int:
        as_bin = bin(n)[2:]
        as_bin = "0" * (32 - len(as_bin)) + as_bin
        return int(as_bin[::-1], 2)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.reverseBits(t) == expected


if __name__ == "__main__":
    s = Solution()
