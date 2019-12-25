from typing import Dict
from testcase import testcase


class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        counter = self._new_counter()
        primitives = []

        start = 0
        for i, s in enumerate(S):
            counter[s] += 1
            if counter.get("(", 0) == counter.get(")", 0):
                if counter.get(s) == 1:
                    primitives.append("")
                else:
                    primitives.append(S[start + 1 : i])
                start = i + 1
                counter = self._new_counter()

        return "".join(primitives)

    def _new_counter(self) -> Dict[str, int]:
        return {"(": 0, ")": 0}


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.removeOuterParentheses(t) == expected


if __name__ == "__main__":
    s = Solution()
    for t, _ in testcase:
        print(s.removeOuterParentheses(t))
