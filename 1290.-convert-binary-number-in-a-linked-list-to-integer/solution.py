from typing import List
from testcase import testcase, ListNode


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        return int("".join(str(x) for x in self.iter(head)), 2)

    def pop(self, head: ListNode) -> int:
        if head.next:
            if head.next.next is None:
                nhead = head.next
                head.next = None
            else:
                nhead = head.next
            return self.pop(nhead)
        else:
            return head.val

    def iter(self, head: ListNode) -> List[int]:
        r = []
        while head.next:
            r.insert(0, self.pop(head))

        r.insert(0, head.val)
        return r


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.getDecimalValue(t) == expected


if __name__ == "__main__":
    s = Solution()
    print(s.iter(testcase[0][0]))
