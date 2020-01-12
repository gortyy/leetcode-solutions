from typing import List
from testcase import testcase


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        total = 0
        num_of_chars = len(chars)
        # Filter out words longer than number of specified characters
        filtered_words = (w for w in words if num_of_chars > len(w))
        for word in filtered_words:
            # Copy of chars, as we're replacing characters
            chars_copy = chars[:]
            # Count of characters that match
            count = 0
            for letter in word:
                if not chars_copy:
                    # Ran out of characters
                    break
                if letter in chars_copy:
                    # Replace character with empty string if we got a match
                    chars_copy = chars_copy.replace(letter, "", 1)
                    count += 1
            else:
                # Perform this check only if `for` got to the end
                if count == len(word):
                    total += count

        return total


def test():
    s = Solution()
    for words, chars, expected in testcase:
        assert s.countCharacters(words, chars) == expected


if __name__ == "__main__":
    s = Solution()
    for words, chars, _ in testcase:
        print(s.countCharacters(words, chars))
