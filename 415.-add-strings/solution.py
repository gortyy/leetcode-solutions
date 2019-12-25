from typing import List
from itertools import zip_longest
from testcase import testcase


class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        added = self.naive_add_strings(num1, num2)
        for i, n in enumerate(added):
            if n >= 10:
                added[i] = n - 10
                ni = i + 1
                if ni == len(added):
                    added.append(1)
                else:
                    added[ni] += 1

        return "".join(str(x) for x in added[::-1])

    def naive_add_strings(self, num1: str, num2: str) -> List[int]:
        if len(num1) < len(num2):
            num1, num2 = num2, num1
        added = []
        for a, b in zip_longest(num1[::-1], num2[::-1]):
            if b is None:
                b = 0
            added.append(int(a) + int(b))
        return added


if __name__ == "__main__":
    s = Solution()
    for x, y in testcase.items():
        print(x == s.addStrings(*y))
