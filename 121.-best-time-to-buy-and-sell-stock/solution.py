from typing import List
from testcase import testcase


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if not prices:
            return 0

        min, min_index = self.min_with_index(prices)
        max, max_index = self.max_with_index(prices)

        while max_index < min_index:
            old = max_index + 1
            max, max_index = self.max_with_index(prices[max_index + 1 :])
            max_index += old

        return max - min

    def min_with_index(self, container: List[int]) -> int:
        result = (container[0], 0)

        for index, elem in enumerate(container[1:]):
            if elem < result[0]:
                result = (container[index + 1], index + 1)

        return result

    def max_with_index(self, container: List[int]) -> int:
        result = (container[0], 0)

        for index, elem in enumerate(container[1:]):
            if elem > result[0]:
                result = (container[index + 1], index + 1)

        return result


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.maxProfit(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.maxProfit(t))
