import sys


def nl():
    file = sys.stdin
    if len(sys.argv) == 2:
        file = open(sys.argv[1], "r")
    for i, line in enumerate(file, start=1):
        print(i, line, end="")


if __name__ == "__main__":
    nl()
