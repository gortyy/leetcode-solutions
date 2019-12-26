from testcase import testcase


class Solution:
    def fib(self, N: int) -> int:
        if N <= 1:
            return N
        fs = [0, 1]
        for i in range(2, N + 1):
            fs.append(fs[i - 1] + fs[i - 2])

        return fs[-1]


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.fib(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.fib(t))
