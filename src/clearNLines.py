LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'


def clearNLines(n: int):
    if n > 0:
        print(LINE_CLEAR, end='')
        for _ in range(n - 1):
            print(LINE_UP, end=LINE_CLEAR)
