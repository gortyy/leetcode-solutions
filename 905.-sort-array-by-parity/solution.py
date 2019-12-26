from typing import List
from testcase import testcase


class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = [], []
        for x in A:
            if x % 2:
                odd.append(x)
            else:
                even.append(x)

        return [*sorted(even), *sorted(odd)]


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.sortArrayByParity(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.sortArrayByParity(t))
