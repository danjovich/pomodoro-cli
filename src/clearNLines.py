LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'


def clearNLines(n: int):
    for _ in range(n):
        print(LINE_UP, end=LINE_CLEAR)
