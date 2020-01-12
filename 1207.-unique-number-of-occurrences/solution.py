from collections import Counter
from typing import List
from testcase import testcase


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        return len(counter) == len(set(v for _, v in counter.items()))


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.uniqueOccurrences(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.uniqueOccurrences(t))
