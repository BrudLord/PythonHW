import sys


def tail():
    if len(sys.argv) == 1:
        lines = sys.stdin.readlines()
        for line in lines[max(len(lines) - 17, 0) :]:
            print(line, end="")
    else:
        for i in sys.argv[1:]:
            if len(sys.argv) > 2:
                print("==> {} <==".format(i))
            lines = open(i, "r").readlines()
            for line in lines[max(len(lines) - 10, 0) :]:
                print(line, end="")
            print()


if __name__ == "__main__":
    tail()
