#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    if len(sys.argv) == 1:
        print(f'0 arguments.')
    else:
        if len(sys.argv) == 2:
            print(f'{len(sys.argv) - 1} argument:')
        else:
            print(f'{len(sys.argv) - 1} arguments:')
        for pos in range(1, len(sys.argv)):
            print(f'{pos}: {sys.argv[pos]}')
