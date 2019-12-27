from testcase import testcase


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        if x < y:
            x, y = y, x
        bx = str(bin(x))[:1:-1]
        by = str(bin(y))[:1:-1]

        while len(by) != len(bx):
            by += "0"
        count = 0
        for a, b in zip(bx, by):
            if a != b:
                count += 1
        return count


def test():
    s = Solution()
    for x, y, expected in testcase:
        assert s.hammingDistance(x, y) == expected


if __name__ == "__main__":
    s = Solution()
    for x, y, _ in testcase:
        print(s.hammingDistance(x, y))
