import sys


def wc():
    if len(sys.argv) == 1:
        txt = sys.stdin.read()
        print(
            txt.count("\n") + (txt and not txt.endswith("\n")),
            len(txt.split()),
            len(txt.encode("utf-8")),
        )
    else:
        word_cnt = 0
        lines_cnt = 0
        bytes_cnt = 0
        for i in sys.argv[1:]:
            current = (
                len(open(i, "r").readlines()),
                len(open(i, "r").read().split()),
                len(open(i, "rb").read()),
            )
            lines_cnt += current[0]
            word_cnt += current[1]
            bytes_cnt += current[2]
            print(*current, i)
        print(lines_cnt, word_cnt, bytes_cnt, "total")


if __name__ == "__main__":
    wc()
