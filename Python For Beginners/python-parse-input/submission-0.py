from typing import List


def read_integers() -> List[int]:
    n = input()
    nh = n.split(",")
    return [int(x) for x in nh]


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())