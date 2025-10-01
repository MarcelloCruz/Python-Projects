import math

def cin(): return int(input())

def cout(n, ok):
    if ok:
        print(n)
    else:
        print("Nu exista")

def prim(n):
    if n < 2: return 0
    elif n == 2: return 1
    elif n > 2 and n % 2 == 0: return 0
    else:
        for d in range(3, int(math.sqrt(n)) + 1, 2):
            if n % d == 0: return 0

    return 1

def main():
    n = cin()
    ok = False

    for i in range(n - 1, 2, -1):
        if prim(i):
            ok = True
            break

    cout(i, ok)

if __name__ == '__main__':
    main()