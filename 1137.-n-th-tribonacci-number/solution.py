from testcase import testcase


class Solution:
    def tribonacci(self, n: int) -> int:
        ts = [0, 1, 1]
        if n <= 2:
            return ts[n]

        for i in range(3, n + 1):
            ts.append(ts[i - 1] + ts[i - 2] + ts[i - 3])

        return ts[-1]


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.tribonacci(t) == expected


if __name__ == "__main__":
    s = Solution()
