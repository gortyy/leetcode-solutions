from typing import List
from testcase import testcase


class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        flipped_and_inverted = []
        for row in A:
            flipped_and_inverted.append(
                [self.invert(x) for x in reversed(row)]
            )

        return flipped_and_inverted

    def invert(self, x: int):
        if x == 0:
            return 1
        else:
            return 0


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.flipAndInvertImage(t) == expected


if __name__ == "__main__":
    s = Solution()
