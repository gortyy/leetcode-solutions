from testcase import testcase


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        if s.find(" ") == -1:
            return len(s)
        r = s[::-1]
        return len(r[: r.find(" ")])


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.lengthOfLastWord(t) == expected


if __name__ == "__main__":
    s = Solution()
