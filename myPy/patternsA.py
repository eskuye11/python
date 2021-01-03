import time


def patterns(n):

    k = n
    print()
    for i in range(0, n):
        for j in range(0, k):
            print(end='  ')
        k = k -1
        for j in range(0, i + 1):
            print(chr(i+65), end='   ')
        print('\r')
        time.sleep(1)

    k = n
    for i in range(0, k):
        for j in range(0, i + 2):
            print(end='  ')
        k = k - 1
        for j in range(0, k):
            print(chr(k+64), end='   ')
        print('\r')
        time.sleep(1)


if __name__ == '__main__':
    patterns(9)
