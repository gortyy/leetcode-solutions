from typing import List
from testcase import testcase


class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        as_string = "".join(str(a) for a in A)
        return [int(as_string[:i], 2) % 5 == 0 for i in range(1, len(A) + 1)]


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.prefixesDivBy5(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.prefixesDivBy5(t))
