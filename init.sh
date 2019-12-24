#!/bin/bash

set -eo pipefail

directory="${1:-}"

directory="$(echo "${1// /-}" | tr '[:upper:]' '[:lower:]')"

mkdir "${directory}"
cd "${directory}"

cat << EOF > solution.py
from testcase import testcase


def test():
    s = Solution()
    for t, expected in testcase:
        assert s.Method(t) == expected


if __name__ == "__main__":
    s = Solution()
EOF

cat << EOF > testcase.py
testcase = []
EOF

code {solution,testcase}.py
