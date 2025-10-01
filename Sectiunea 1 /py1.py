import math

def cin(): return int(input())
def cout(numar): print(numar)

def prim(n):
    if n < 2:
        return 0

    elif n == 2:
        return 1

    elif n % 2 == 0 and n > 2:
        return 0

    else:
        for d in range(3, int(math.sqrt(n)) + 1):
            if n % d == 0:
                return 0

        return 1


def main():
    n = cin()

    while not(prim(n)):
        n += 1

    cout(n)

if __name__ == '__main__':
  main()
