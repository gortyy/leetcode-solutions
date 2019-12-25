from testcase import testcase


class Solution:
    def firstUniqChar(self, s: str) -> int:
        return self.two_pass(s)

    def two_pass(self, s: str) -> int:
        counter = {}
        for c in s:
            if counter.get(c) is not None:
                counter[c] += 1
            else:
                counter[c] = 1

        for c, count in counter.items():
            if count == 1:
                return s.find(c)
        return -1

    def naive(self, s: str) -> int:
        if len(s) == 1:
            return 0
        if len(s) == 2:
            if s[0] == s[1]:
                return -1
            return 0

        cs = []

        for i, c in enumerate(s):
            subs = s[i + 1 :]
            if len(subs) == 1 and subs not in cs:
                if s[-1] != s[-2]:
                    if s[-2] not in cs:
                        return i
                    return i + 1
            if subs and subs.find(c) == -1 and c not in cs:
                return i
            cs.append(c)

        return -1


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.firstUniqChar(t) == expected


if __name__ == "__main__":
    s = Solution()
