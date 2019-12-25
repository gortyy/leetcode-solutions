from testcase import testcase


class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace(".", "[.]")


if __name__ == "__main__":
    s = Solution()
    for t in testcase:
        print(s.defangIPaddr(t))
