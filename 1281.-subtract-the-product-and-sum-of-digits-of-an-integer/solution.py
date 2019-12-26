from operator import mul
from functools import reduce
from testcase import testcase


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        sequence = [int(s) for s in str(n)]
        return self.product(sequence) - self.sum(sequence)

    def product(self, s) -> int:
        return reduce(mul, s)

    def sum(self, s) -> int:
        return sum(s)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.subtractProductAndSum(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.subtractProductAndSum(t))
