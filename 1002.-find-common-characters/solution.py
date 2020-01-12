from typing import List
from testcase import testcase


class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        uniques = set.intersection(*[set(a) for a in A])
        counter = dict()
        for word in A:
            counter[word] = dict()
            for unique in uniques:
                c = sum(1 for letter in word if letter == unique)
                counter[word][unique] = c

        longest_word = len(sorted(A, key=len)[0])
        minimums = {unique: longest_word for unique in uniques}

        for _, v in counter.items():
            for u, m in v.items():
                minimums[u] = min(m, minimums[u])

        result = []
        for k, v in minimums.items():
            result.extend([k] * v)

        return sorted(result)


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.commonChars(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.commonChars(t))
