g = globals()


def assign(*args):
    g[args[0][0]] = args[0][1]


def show(*args):
    print(g[args[0][0]])


def equal(*args):
    if args[0][0] in g and args[0][1] in g:
        # both args are variables
        print("yes" if g[args[0][0]] == g[args[0][1]] else "no")
    elif args[0][0] in g:
        # second arg is a value
        print("yes" if g[args[0][0]] == args[0][1] else "no")
    else:
        # both args are values
        print("yes" if args[0][0] == args[0][1] else "no")


def minus(*args):
    x, _, y = args[0]
    if x in g and y in g:
        # both args are variables
        g[y] = int(g[y]) - int(g[x])
    elif x in g:
        # second arg is a value -- x - 3
        # TODO
        pass
    elif y in g:
        # first arg is a value
        g[y] = int(g[y]) - int(x)
    else:
        # both args are values
        # TODO
        pass
