from typing import List
from testcase import testcase


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = dict()
        id = 0
        for gs in groupSizes:
            g = groups.get(gs)
            if g:
                g.append(id)
            else:
                groups[gs] = [id]
            id += 1

        result = []
        for g, ids in groups.items():
            if len(ids) > g:
                start = 0
                for i in range(g, len(ids) + 1, g):
                    result.append(ids[start:i])
                    start = i
            else:
                result.append(ids)
        return result


def test():
    s = Solution()
    # These tests won't pass, but its working
    for t, expected in testcase:
        assert s.groupThePeople(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.groupThePeople(t))
