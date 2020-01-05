from typing import List
from testcase import testcase


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict()
        for word in words:
            if d.get(word):
                d[word] += 1
            else:
                d[word] = 1

        counts = dict()
        for word, count in sorted(d.items(), reverse=True, key=lambda x: x[1]):
            if counts.get(count):
                counts[count].append(word)
            else:
                counts[count] = [word]

        result = list()
        for _, item in sorted(counts.items(), reverse=True):
            result.extend(sorted(item))
        return result[:k]


def test():
    s = Solution()
    for words, k, expected in testcase:
        assert s.topKFrequent(words, k) == expected


if __name__ == "__main__":
    s = Solution()
    for words, k, _ in testcase:
        print(s.topKFrequent(words, k))
