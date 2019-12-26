from typing import List
from testcase import testcase


class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num % 2:
            return False
        return self.summed(num) == num

    def summed(self, num: int) -> List[int]:
        summed = 0
        for d in range(1, num // 2 + 1):
            if num % d == 0:
                summed += d
        return summed


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.checkPerfectNumber(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.checkPerfectNumber(t))
