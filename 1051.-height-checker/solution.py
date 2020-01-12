from typing import List
from testcase import testcase


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        return sum(1 for a, b in zip(heights, sorted(heights)) if a != b)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.heightChecker(t) == expected


if __name__ == "__main__":
    s = Solution()
