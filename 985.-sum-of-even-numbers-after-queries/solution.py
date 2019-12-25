from typing import List
from testcase import testcase


class Solution:
    def sumEvenAfterQueries(
        self, A: List[int], queries: List[List[int]]
    ) -> List[int]:
        result = []
        summed = sum(x for x in A if x % 2 == 0)
        for v, i in queries:
            if A[i] % 2 == 0:
                summed -= A[i]
            A[i] += v
            if A[i] % 2 == 0:
                summed += A[i]
            result.append(summed)

        return result


def test():
    s = Solution()
    for t, q, expected in testcase:
        assert s.sumEvenAfterQueries(t, q) == expected


if __name__ == "__main__":
    from pprint import pprint

    s = Solution()
    for t, q, expected in testcase:
        pprint(s.sumEvenAfterQueries(t, q))
