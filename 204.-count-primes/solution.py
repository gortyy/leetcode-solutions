from math import factorial, sqrt
from testcase import testcase


class Solution:
    def countPrimes(self, n: int) -> int:
        return self.fast(n)

    def formula(self, n: int) -> int:
        return len([x for x in range(2, n) if factorial(x - 1) % x == x - 1])

    def naive(self, n: int) -> int:
        if n > 2:
            box = [2]
        else:
            return 0
        for x in range(3, n):
            if all(x % y for y in box):
                box.append(x)

        return len(box)

    def fast(self, n: int) -> int:
        if n <= 2:
            return 0

        box = [x for x in range(2, n)]

        for i in range(round(sqrt(n)) - 1):
            x = box[i]
            if x == 0:
                continue
            for j in range(i + x, len(box), x):
                box[j] = 0

        return len([x for x in box if x != 0])


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.countPrimes(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.countPrimes(t))
