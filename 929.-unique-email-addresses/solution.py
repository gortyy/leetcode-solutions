from typing import List
from testcase import testcase


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        uniq = set()
        for email in emails:
            uniq.add(self.process(email))

        return len(uniq)

    def process(self, email: str) -> str:
        localname, domain = email.lower().split("@")
        localname = localname.split("+")[0].replace(".", "")
        return "@".join((localname, domain))


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.numUniqueEmails(t) == expected


if __name__ == "__main__":
    s = Solution()
