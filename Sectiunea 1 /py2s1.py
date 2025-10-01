import math

def prim(n):
    if n < 2:
        return 0
    elif n == 2:
        return 1
    elif n > 2 and n % 2 == 0:
        return 0
    else:
        for d in range(3, int(math.sqrt(n)) + 1, 2):
            if n % d == 0:
                return 0

    return 1

def cin(): return int(input())
def cout(x, y): print(x, y)
def caz2(): print("Nu exista")

def main():
    n = cin()
    x = False

    for i in range(2, n, 1):
        if prim(i):
            if (prim(n - i)):
                cout(i, n - i)
                x = True
                break

    if not x:
        caz2()

if __name__ == '__main__':
    main()