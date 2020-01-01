from itertools import combinations
from typing import List
from testcase import testcase


class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        if not nums:
            return 0
        bins = [str(bin(n))[:1:-1] for n in nums]
        longest = max(bins, key=len)

        longest_len = len(longest)
        for i, _ in enumerate(bins):
            bins[i] += "0" * (longest_len - len(bins[i]))
            bins[i] = [int(s) for s in list(bins[i])]

        return sum(
            self.hammingDistance(a, b) for a, b in combinations(bins, 2)
        )

    def hammingDistance(self, bx: List[int], by: List[int]) -> int:
        count = 0
        for a, b in zip(bx, by):
            if a != b:
                count += 1
        return count


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.totalHammingDistance(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(len(t))
        print(len(set(t)))
        print(s.totalHammingDistance(t))
