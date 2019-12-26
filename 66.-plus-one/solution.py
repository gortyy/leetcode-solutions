from typing import List
from testcase import testcase


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digits[-1] += 1
        digits = digits[::-1]
        for i, d in enumerate(digits):
            if d >= 10:
                digits[i] -= 10
                next_i = i + 1
                if next_i == len(digits):
                    digits.append(1)
                else:
                    digits[next_i] += 1
        return digits[::-1]


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.plusOne(t) == expected


if __name__ == "__main__":
    s = Solution()
    print(s.plusOne([1, 2, 9]))
