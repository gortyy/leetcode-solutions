from typing import List
from testcase import testcase


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        return [n for n in range(left, right + 1) if self.is_self_divisible(n)]

    def is_self_divisible(self, n: int) -> bool:
        as_string = str(n)
        if "0" in as_string:
            return False

        for u in (int(u) for u in as_string if u != "1"):
            if int(as_string) % u != 0:
                return False

        return True


def test():
    s = Solution()
    for l, r, expected in testcase:
        assert s.selfDividingNumbers(l, r) == expected


if __name__ == "__main__":
    s = Solution()
    for l, r, _ in testcase:
        print(s.selfDividingNumbers(l, r))
