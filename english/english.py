import argparse
import commands

cmds = {
    'make': commands.assign,
    'show': commands.show,
    'is': commands.equal,
    'subtract': commands.minus
}
is_parsing = True


def main():
    parser = create_parser()
    args = parser.parse_args()

    with open(args.engfile) as f:
        for line in f:
            if line.strip() and not line.startswith('comment:'):
                parse_line(line.strip())


def parse_line(line):
    global is_parsing
    if line.startswith('comments:'):
        is_parsing = False
    if is_parsing:
        ops = line.split()
        c = ops[0]  # the command to interpret
        cmds[c](ops[1:])
    if line == 'end comments':
        is_parsing = True


def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('engfile', help="English file to interpret")
    return parser


if __name__ == '__main__':
    main()
