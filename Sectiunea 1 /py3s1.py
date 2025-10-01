def cin(): return int(input())
def cout(n): print(n)

def main():
    n = cin()

    digitlist = []

    while n > 0:
        digit = n % 10
        digitlist.append(digit)
        n //= 10

    digitlist.sort()
    digitlist.reverse()

    numar = 0
    for digit in digitlist:
        numar = numar * 10 + digit

    cout(numar)

if __name__ == '__main__':
    main()