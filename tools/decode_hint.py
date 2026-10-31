# Hollowmere buffer utility
#
# This script was recovered from the development
# workstation.
#
# It attempts to convert hexadecimal buffer
# values into readable ASCII characters.
#
# It does not perform any authentication or
# flag extraction.

import sys

def decode(data):

    output = []

    for value in data:

        if value in ("00", "ff"):
            continue

        try:

            output.append(
                chr(int(value, 16))
            )

        except ValueError:

            continue

    return "".join(output)

if __name__ == "__main__":

    raw = sys.stdin.read().split()

    print(decode(raw))
