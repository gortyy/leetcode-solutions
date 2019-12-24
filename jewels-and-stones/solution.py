from testcase import testcase


class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        total = 0
        for s in S:
            if s in J:
                total += 1
        return total


def test():
    solution = Solution()
    for j, s, expected in testcase:
        assert solution.numJewelsInStones(j, s) == expected


if __name__ == "__main__":
    sol = Solution()
    for j, s, e in testcase.items():
        assert e == sol.numJewelsInStones(j, s)
