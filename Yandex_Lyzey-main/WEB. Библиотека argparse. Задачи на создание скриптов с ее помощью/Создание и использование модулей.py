import argparse
import sys


def count_lines(filename):
    cnt = 0
    try:
        f = open(filename)
        for line in f:
            cnt += 1
    except BaseException:
        cnt = 0
    return cnt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description="number of lines in the file")
    parser.add_argument('--file', default=sys.stdout, type=str,
                        help='the input file name')
    args = parser.parse_args()
    print(count_lines(args.file))
