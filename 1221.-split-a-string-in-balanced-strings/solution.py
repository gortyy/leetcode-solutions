from testcase import testcase


class Solution:
    def balancedStringSplit(self, s: str) -> int:
        count, start = 0, 0
        increment = 2
        for x in range(2, len(s) + 1, increment):
            if self.balanced(s[start:x]):
                start = x
                count += 1
            else:
                increment *= 2

        return count

    def balanced(self, s: str) -> int:
        s = "".join(sorted(s))
        r_pos = s.find("R")
        if r_pos == -1 or s.find("L") == -1:
            return False
        ls = s[:r_pos]
        rs = s[r_pos:]

        return len(ls) == len(rs)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.balancedStringSplit(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.balancedStringSplit(t))
