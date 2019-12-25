from typing import List
from itertools import zip_longest
from testcase import testcase


class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        K = self.to_array_form(K)

        initial = []
        for a, b in zip_longest(A[::-1], K[::-1]):
            if a is None:
                a = 0
            if b is None:
                b = 0
            initial.append(a + b)

        for i, n in enumerate(initial):
            if n >= 10:
                initial[i] = n - 10
                next_i = i + 1
                if next_i == len(initial):
                    initial.append(1)
                else:
                    initial[next_i] += 1

        return initial[::-1]

    def to_array_form(self, i: int) -> List[int]:
        as_string = str(i)
        return [int(x) for x in as_string]


def test():
    s = Solution()
    for A, K, expected in testcase:
        assert s.addToArrayForm(A, K) == expected


if __name__ == "__main__":
    pass
