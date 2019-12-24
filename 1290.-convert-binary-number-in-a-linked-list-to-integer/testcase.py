class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def build_list_node(l):
    nl = ListNode(l[0])
    head = nl
    for e in l[1:]:
        nhead = ListNode(e)
        head.next = nhead
        head = nhead
    return nl


testcase = [
    (build_list_node([1, 0, 1]), 5),
    (build_list_node([0]), 0),
    (build_list_node([1]), 1),
    (build_list_node([1, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0]), 18880),
    (build_list_node([0, 0]), 0),
]
