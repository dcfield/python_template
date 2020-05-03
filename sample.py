import sys
import argparse

parser=argparse.ArgumentParser(
    description='''Here is the description for my beautiful new script.''',
    epilog="""All for one and one for all.""")
parser.add_argument('--a', type=int, default=42, help='a is for apple.')
parser.add_argument('b', nargs='*', default=[1, 2, 3], help='b is a positional argument.')
args=parser.parse_args()


def main():
    print("Run `sample.py --help`")


if __name__ == '__main__':
    args = sys.argv
    main()