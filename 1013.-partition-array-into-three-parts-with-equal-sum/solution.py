from typing import List
from testcase import testcase


class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        sum_of_a = sum(A)
        if sum_of_a % 3 != 0:
            return False

        equal_part = sum_of_a / 3

        def check_sublist(A: List[int]) -> int:
            part = 0
            for i, e in enumerate(A):
                part += e
                if part == equal_part:
                    break
            else:
                raise ValueError
            return i + 1

        try:
            first_index = check_sublist(A)
            second_index = check_sublist(A[first_index:])
        except ValueError:
            return False

        third_part = sum(A[first_index + second_index :])
        return third_part == equal_part


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.canThreePartsEqualSum(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.canThreePartsEqualSum(t))
